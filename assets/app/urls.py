from django.urls import path
from .import views
from .views import blogpost,blogdetail

urlpatterns = [
    path('',views.home, name="home"),
    path('blogpost',blogpost.as_view(), name="post"),
    path('postdetail/<int:pk>',blogdetail.as_view(), name="blogdetail"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('login',views.login, name="login"),
    path('register',views.register, name="register"),
    
]