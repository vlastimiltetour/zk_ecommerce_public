from inspect import formatargspec
from .models import Subscribers, MailMessage
from django import forms
from . import views

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email']



class MailMessagesForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'