from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from account.serializers import RegistrationSerializer, CreateNewPasswordSerializer
from account.utils import send_activation_code
from .models import User

class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Регистрация прошла успешно', 201)

class ActivationView(APIView):
    def get(self, request, activation_code):
        User = get_user_model()
        user = get_object_or_404(User, activation_code=activation_code)

        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response("Ваш аккаунт активирован", 200)

class LogOutView(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        refresh_token = self.request.data['refresh_token']
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response("Вы вышли из своего аккаунта", status=205)










class ForgotPasswordView(APIView):
    def get(self, request, email):
        user = get_object_or_404(User, email=email)
        user.is_active = False
        user.create_activation_code()
        user.save()
        send_activation_code(
            email=user.email, activation_code=user.activation_code,
            status='forgot_password'
        )
        return Response('Вам отпаравили письмо на почту', status=200)


class CompleteRestPasswordView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = CreateNewPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Вы успешно поменяли пароль', status=200
            )



