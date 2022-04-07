from django.urls import path
from .views import resize, home

urlpatterns = [
    # path('', home, name='home'),
    path('resize', resize, name='resize'),
]