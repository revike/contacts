from rest_framework import serializers

from contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Serializer for contacts"""
    email = serializers.EmailField(source='get_email')

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'phone', 'created', 'updated', 'email',)
