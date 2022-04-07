from django.urls import path
from .views import resize

urlpatterns = [
    path('resize', resize, name='resize'),
]