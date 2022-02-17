from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from account.views import RegistrationView, ActivationView, LogOutView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('logout/', LogOutView.as_view()),
    # path('refresh/', TokenRefreshView.as_view()),
]