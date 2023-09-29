from django.db import models
from operator import mod
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class OrserStauts(models.TextChoices):
   PROCESSING = "Processing"
   SHIPPED  = "Shipped"
   DELIVERED = "Delivered"

class PaymentStauts(models.TextChoices):
   PAID = "Paid"
   UNPAID = "Unpaid"

class PaymentMode(models.TextChoices):
   COD = "Cod"
   CARD = "Card"

class Order(models.Model):
   city = models.CharField(max_length=400,default="",blank=False)
   zip_code = models.CharField(max_length=100,default="",blank=False)
   street = models.CharField(max_length=500,default="",blank=False)
   state = models.CharField(max_length=100,default="",blank=False)
   country =  models.CharField(max_length=100,default="",blank=False)
   phone_no = models.CharField(max_length=100,default="",blank=False)
   total_amount = models.IntegerField(default=0)
   payment_stauts =  models.CharField(max_length=30,choices=PaymentStauts.choices,default=PaymentStauts.UNPAID)
   payment_mode =  models.CharField(max_length=30,choices=PaymentMode.choices,default=PaymentMode.COD)
   stauts =   models.CharField(max_length=30,choices=OrserStauts.choices,default=OrserStauts.PROCESSING)
   user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL) 
   createAt =models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return str(self.id)
   

class OrderItem(models.Model):
   product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL) 
   oredr = models.ForeignKey(Order,null=True,on_delete=models.CASCADE,related_name="orderitems")
   name = models.CharField(max_length=200,default="",blank=False)
   quantity = models.IntegerField(default=1)
   price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)

   def __str__(self):
      return self.name