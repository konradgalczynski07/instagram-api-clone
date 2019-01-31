from rest_framework import generics, authentication, permissions, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth import get_user_model
from user.serializers import UserInfoSerializer, AuthTokenSerializer, \
    RegisterUserSerializer, UserProfileSerializer


class RegisterUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = RegisterUserSerializer


class LoginUserView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user account info"""
    serializer_class = UserInfoSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


class UserProfileView(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = get_user_model().objects.all()
    serializer_class = UserProfileSerializer
