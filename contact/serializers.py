from rest_framework import serializers

from contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Serializer for contacts"""
    email = serializers.EmailField(source='get_email')

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'phone', 'created', 'updated', 'email',)

    def update(self, instance, validated_data):
        email = validated_data.get('get_email')
        if email:
            instance.contact_data.email = email
            instance.contact_data.save()
        return super().update(instance, validated_data)
