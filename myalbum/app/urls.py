from django.urls import path
from .views import resize, ApiResize

urlpatterns = [
    path('resize', resize, name='resize'),
    path('api/resize', ApiResize.as_view()),
]