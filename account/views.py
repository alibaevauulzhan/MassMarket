from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from account.serializers import RegistrationSerializer


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