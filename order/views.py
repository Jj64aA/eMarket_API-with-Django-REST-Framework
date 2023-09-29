
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from django.db.models import Avg

from product.models import Product

from .serializers import OrderItemsSerializer , OrderSerializer

from .models import Order , OrderItem
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
   orders = Order.objects.all()
   serializer = OrderSerializer(orders,many=True)
   return Response({"orders":serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request,pk):
   order = get_object_or_404(Order, id=pk)
   serializer = OrderSerializer(order,many=False)
   return Response({"order":serializer.data})

@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_order(request,pk):
   order = get_object_or_404(Order, id=pk)
   order.stauts = request.data["stauts"]
   order.save()
   return Response({"order":"Order is Updated"})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order(request,pk):
   order = get_object_or_404(Order, id=pk)
   order.delete()
   return Response({"details":"Order is Deleted "})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_order(request):
   user = request.user
   data = request.data 
   order_items = data["order_Items"]

   if order_items and len(order_items) == 0  : 
      return Response({'error':'No Order recieved'},status=status.HTTP_400_BAD_REQUEST)
   
   else : 
      total_amount =  sum( float(item['price']) * int(item['quantity']) for item in order_items  )
      order = Order.objects.create(
         user = user,
         city = data['city'],
         zip_code = data['zip_code'],
         street = data['street'],
         phone_no = data['phone_no'],
         country = data['country'],
         total_amount = total_amount,
      )
      for i in order_items : 
         product = Product.objects.get(id=i['product'])
         item = OrderItem.objects.create(
            product = product,
            oredr = order , 
            name = product.name , 
            quantity = i["quantity"] , 
            price  = i['price']
         )
         product.stock -= item.quantity 
         product.save()

      serializer = OrderSerializer(order,many=False)
      return Response(serializer.data)
   