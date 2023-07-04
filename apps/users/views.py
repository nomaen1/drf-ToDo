from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated


from apps.users.serializers import UserSerializer, UserRegisterSerializer, UserDetailSerializer
from apps.users.models import User

class UsersAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, ) 
    
    def get_serializer_class(self):
        if self.action in ('create', ):
            return UserRegisterSerializer
        elif self.action in ('retrieve', ):
            return UserDetailSerializer
        return UserSerializer