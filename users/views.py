from rest_framework import generics

from users.serializers import RegisterSerializer


class RegisterApiView(generics.CreateAPIView):
    """Register user"""
    serializer_class = RegisterSerializer
