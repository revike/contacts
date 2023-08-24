from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import RegisterApiView

app_name = 'users'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterApiView.as_view(), name='register'),
]
