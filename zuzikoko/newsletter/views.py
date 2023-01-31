from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubscribersForm, MailMessagesForm
from .models import Subscribers, MailMessage
from django.http import request, response
from django.http import HttpResponse
from cart.forms import CartAddProductForm
from django.db.models import Q 
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame


# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        print(request.POST)
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Subscription Successful')
            return redirect('/')

    else:
        form = SubscribersForm()
    
    context = {'form': form}
    
    return render(request, '/', context)



def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    
    if request.method == 'POST':
        form = MailMessagesForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )

        messages.success(request, 'Message has been sent to the Mail List')
        return redirect('newsletter:mail_letter')

    else:
        form = MailMessagesForm()
    context = {'form': form}

    
    return render(request, 'newsletter/mail.html', context)
