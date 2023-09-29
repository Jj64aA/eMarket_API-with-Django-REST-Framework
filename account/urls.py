from django.urls import path,include 
from  . import views 

urlpatterns = [
   path('register/',views.register,name="register"),
   path('userinfo/',views.current_user,name="userinfo"),
   path('userinfo/update',views.update_user,name="userinfo-update"),
   path('forgot_password/',views.forgot_password,name="forgot_password"),
   path('reset_password/<str:token>',views.reset_password,name="reset_password"),
] 