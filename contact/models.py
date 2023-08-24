from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from config.settings import AUTH_USER_MODEL as USER
from base.models import BaseModel, NULLABLE
from contact.validators import validate_phone


class Contact(BaseModel):
    """Contact model"""
    author = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='contact_user', verbose_name=_('user'))
    first_name = models.CharField(_('first name'), max_length=64, **NULLABLE)
    last_name = models.CharField(_('last name'), max_length=64, **NULLABLE)
    phone = models.CharField(_('phone'), max_length=16, validators=[validate_phone])
    is_active = models.BooleanField(_('is active'), default=True)

    def __str__(self):
        if not self.first_name and not self.last_name:
            return f'{self.phone}'
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['first_name', 'last_name']

    def get_email(self):
        return self.contact_data.email


class ContactData(BaseModel):
    """Contact Data model"""
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE,
                                   related_name='contact_data', verbose_name=_('contact'))
    email = models.EmailField(_('email'), **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'contact data'
        verbose_name_plural = 'contacts data'

    @staticmethod
    @receiver(post_save, sender=Contact)
    def create_contact_data(sender, instance, created, **kwargs):
        if created and sender == Contact and kwargs:
            ContactData.objects.create(contact=instance)
