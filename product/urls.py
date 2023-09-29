from django.urls import path,include 
from  . import views 

urlpatterns = [
    path('products/',views.get_all_products,name="all_products"),
    path('products/<str:pk>/',views.get__product,name="get_product"),
    path('home/',views.home,name="home"),
    path('details-product/<str:pk>',views.details,name="details-product"),
    path('products/new-product',views.new_product,name="new_product"),
    path("<str:pk>/reviews",views.create_review, name="create_review"),
    path("<str:pk>/reviews/delete",views.delete_review, name="delete_review"),
    path('products/update-product/<str:pk>',views.update_product,name="update-product"),
    path('products/delete-product/<str:pk>',views.delete_product,name="delete-product"),
]
