from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('new_room/', views.room_create, name='new_room'),
    path('<slug:slug>/', views.room, name='room'),
]