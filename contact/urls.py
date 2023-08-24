from django.urls import path

from contact.views import ContactListApiView

app_name = 'contact'

urlpatterns = [
    path('list/', ContactListApiView.as_view(), name='list'),
]
