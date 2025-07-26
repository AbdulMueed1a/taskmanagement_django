from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('statistics/', views.task_statistics, name='task-statistics'),
    path('<int:pk>/status/', views.update_task_status, name='update-task-status'),
]