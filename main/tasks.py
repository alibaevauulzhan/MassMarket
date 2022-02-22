from django.core.mail import send_mail

from MassMarket.celery import app

@app.task
def notify_user(email):
    send_mail(
        'Вы создали новый запрос!',
        'Спасибо за использование нашего сайта!',
        email,
        [email]
    )
    return 'Success'