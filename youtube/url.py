from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('Search', views.search, name='search')
]

urlpatterns = format_suffix_patterns(urlpatterns)