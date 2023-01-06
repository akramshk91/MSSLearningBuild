from django.contrib import admin
from django.urls import path
from home import views
#from main.views import *

#handler404='main.views.handler404' #added manually

#app_name="main"

urlpatterns = [
    path('',views.index,name="Home"),
    path("about",views.about,name="about.html"),
    path("contact",views.contact,name="contact.html"),
    path("modules",views.modules,name="modules"),
    path("test",views.test,name="test.html"),
    path("price",views.price,name="price"),
]
