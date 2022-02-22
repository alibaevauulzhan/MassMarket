
from django.core.mail import send_mail


def send_activation_code(email, activation_code, status):
    if status == 'register':
        activation_url = f"http://localhost:8000/account/activate/{activation_code}"
        message = f"""
        Поздравляем! Вы зарегестрированы на нашем сайте.
        Пройдите активацию вашего аккаунта по ссылке: {activation_url}
        """
        send_mail(
            'Активация аккаунта',
            message,
            'test@gmail.com',
            [email, ],
            fail_silently=False
        )
    elif status == "forgot_password":
        send_mail(
            'Восстановление пароля',
            f"Код активации : {activation_code}",
            'stack_overflow@admin.com',
            [email],
            fail_silently=True
        )