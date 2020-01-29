from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TodoView

todo_list = TodoView.as_view({
    'post': 'create',
    'get': 'list'
})

todo_detail = TodoView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('todos/', todo_list, name='todo_list'),
    path('todos/<int:pk>/', todo_detail, name='todo_detail'),
])
