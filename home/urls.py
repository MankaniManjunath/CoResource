from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about/",views.about,name='about'),
    path("resources/",views.resources,name='resources'),
    path("feedback",views.feedback,name="feedback"),
    #path("model/",views.model,name='model'),   
]