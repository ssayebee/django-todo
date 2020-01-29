from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import permissions

class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)	
