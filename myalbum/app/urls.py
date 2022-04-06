from django.urls import path
from .views import resize_picture

urlpatterns = [
    path('resize', resize_picture, name='resize_picture'),
]