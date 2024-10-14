from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
]