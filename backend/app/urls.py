from django.contrib import admin
from django.urls import path

from .views import add_Employee,view_Employee,update_Employee,delete_Employee

urlpatterns=[
    path('add_Employee/',add_Employee,name="add"),
    path('view_Employee/',view_Employee,name="list"),
    path('Update_Employee/<int:id>',update_Employee),
    path('delete_Employee/<int:id>',delete_Employee),
]