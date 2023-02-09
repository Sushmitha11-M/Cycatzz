from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.student_list),
    path('<str:name>', views.student_name)
]

urlpatterns = format_suffix_patterns(urlpatterns)