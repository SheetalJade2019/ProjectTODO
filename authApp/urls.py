from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login_url,name="login"),
    path('todohome/',views.todohome,name="todohome"),
    path('logout/',views.logout_url,name="logout"),
    path('about/',views.about,name="about"),
    path('contactus/',views.contactus,name="contactus"),
    path('deleteTodo/<int:id>/',views.deleteTodo,name="deleteTodo"),
    path('addTodo/',views.addTodo,name="addTodo"),

]
