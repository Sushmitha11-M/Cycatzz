from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register, name='register'),
    path('success', views.success, name="success")
]