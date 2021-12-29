from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home_page(request):
  return render(request,"index.html")

#Sending Email
def send_gmail(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        message = request.POST.get("message")    
        send_mail(
            subject,
            message,
            'from@mail.com',
            ['to@mail.com'],
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse('email_sender:home'))
    else:
        return HttpResponse('invalid request')
