from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("shonen", views.shonen, name="shonen"),
    path("shojo", views.shojo, name="shojo"),
    path("isekai", views.isekai, name="isekai")
]
