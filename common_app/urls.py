from django.urls import path
from common_app import views


urlpatterns = [
    path('', views.index, name='index'),
]