from django.urls import path
from .views import ListTasks, AddTask, EditTask, DeleteTask

urlpatterns = [
    path('', ListTasks.as_view(), name='tasks'),
    path('add-task/', AddTask.as_view(), name='add-task'),
    path('edit-task/<int:pk>', EditTask.as_view(), name='edit-task'),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task'),
    
]