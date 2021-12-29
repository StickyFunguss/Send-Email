from django.urls import path
from .views import home_page,send_gmail
app_name = 'email_sender'


urlpatterns = [
    path('home/',home_page, name='home'),
    path('send_mail/',send_gmail, name="send_mail")
]