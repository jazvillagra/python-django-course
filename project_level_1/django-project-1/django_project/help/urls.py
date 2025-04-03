
from django.urls import path
from help import views

urlpatterns = [
    path('', views.index, name='index'),
]