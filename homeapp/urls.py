from django.urls import path

from . import views

urlpatterns = [
    path('a/', views.index),
    path('b/', views.myfirstfunc),
    path('c/', views.mySecondfunc)
]