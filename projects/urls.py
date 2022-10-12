from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<int:id>/', views.topic, name='topic'),
]