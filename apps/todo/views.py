from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.todo.permissions import IsOwnerPermissions
from apps.todo.serializers import ToDoSerializer
from apps.todo.models import ToDo

class ToDoAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user) 

    def get_permissioins(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsOwnerPermissions, )
        return (AllowAny(), )