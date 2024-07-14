from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('generate_pdf/<int:session_id>/', views.generate_pdf, name='generate_pdf'),

]
