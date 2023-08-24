from django.urls import path

from contact.views import ContactListApiView, ContactDetailApiView, ContactDeleteApiView

app_name = 'contact'

urlpatterns = [
    path('list/', ContactListApiView.as_view(), name='list'),
    path('<int:pk>/', ContactDetailApiView.as_view(), name='detail'),
    path('delete/<int:pk>/', ContactDeleteApiView.as_view(), name='delete'),
]
