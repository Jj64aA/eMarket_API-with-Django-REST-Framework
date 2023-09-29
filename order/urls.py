from django.urls import path,include 
from  . import views 

urlpatterns = [
      path('orders/new/',views.new_order,name="new_order"),
      path('orders/',views.get_orders,name="get_orders"),
      path('orders/<str:pk>/',views.get_order,name="get_order"),
      path('orders/<str:pk>/process/',views.update_order,name="update_order"),
      path('orders/<str:pk>/delete/',views.delete_order,name="delete_order"),
]   