from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='log_out'),
    path('login/', CustomLoginView.as_view(), name='login'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task-detail'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]
