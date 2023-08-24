from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse, path
from django.utils.html import format_html

from contact.models import Contact, ContactData


class ContactDataInline(admin.StackedInline):
    """Contact Data inline"""
    model = ContactData

    def has_delete_permission(self, request, obj=None):
        pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact admin panel"""
    list_display = ['id', 'first_name', 'last_name', 'phone', 'email', 'is_active', 'is_active_actions']
    list_display_links = list_display
    search_fields = ['first_name', 'last_name', 'contact_data__email', 'author__email']
    list_filter = ['author__email']

    def get_inlines(self, request, obj):
        if obj:
            return [ContactDataInline]
        return super().get_inlines(request, obj)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/active/', self.admin_site.admin_view(self.activate), name='activate'),
            path('<int:pk>/deactive/', self.admin_site.admin_view(self.deactivate), name='deactivate'),
        ]
        return custom_urls + urls

    @classmethod
    def is_active_actions(cls, obj):
        if obj.is_active:
            return format_html(
                '<a class="button" href="{}">Deactivate</a> ', reverse('admin:deactivate', kwargs={'pk': obj.id})
            )
        return format_html(
            '<a class="button" href="{}">Activate</a>', reverse('admin:activate', kwargs={'pk': obj.id})
        )

    @classmethod
    def email(cls, obj):
        return obj.contact_data.email

    @classmethod
    def activate(cls, request, pk):
        review = Contact.objects.get(id=pk)
        review.is_active = True
        review.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    @classmethod
    def deactivate(cls, request, pk):
        review = Contact.objects.get(id=pk)
        review.is_active = False
        review.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


