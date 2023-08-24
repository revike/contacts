from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from contact.filters import ContactFilter
from contact.models import Contact
from contact.paginations import ContactPagination
from contact.serializers import ContactSerializer


class ContactListApiView(generics.ListAPIView):
    """Contact list"""
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    pagination_class = ContactPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContactFilter

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(author=user, is_active=True)


class ContactDetailApiView(generics.RetrieveAPIView, generics.UpdateAPIView):
    """Contact detail"""
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(author=user, is_active=True)


class ContactDeleteApiView(generics.DestroyAPIView):
    """Contact delete"""
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(author=user, is_active=True)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
