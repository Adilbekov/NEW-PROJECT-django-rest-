from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from apps.user.serializer import UserSerializer, UserRegisterSerializer, UserDetileSerializer
from apps.user.models import User

class UserViewSet(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        if self.action == 'retrieve':
            return UserDetileSerializer
        return UserSerializer
    
    def perform_update(self, serializer):
        return serializer.save(user = self.request.user)