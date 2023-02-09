from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import os
# Create your views here.

def Register(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Email_address = request.POST['Email']
        DateofBirth = request.POST['dateofbirth']
        Phone_number = request.POST['phone']

        if User.objects.filter(Name=Name).exists():
            messages.info(request, 'Username already exist')
        elif User.objects.filter(Email_Address=Email_address).exists():
            messages.info(request, 'Email was already taken')
            return redirect("Register")
        else:
            obj = User()
            obj.Name = Name
            obj.Email_Address = Email_address
            obj.DateofBirth = DateofBirth
            obj.Phone_number = Phone_number
            mydict = {'name': Name}
            obj.save()
            html_template = 'email_register.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Welcome to Service-Verse'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [Email_address]
            message = EmailMessage(subject, html_message, email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            print(os.environ.get("EMAIL_USER"))
            return redirect("success")

    return render(request, 'login_page.html')

def success(request):
    return render(request, 'success.html')


