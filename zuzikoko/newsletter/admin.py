from django.contrib import admin
from .models import Subscribers, MailMessage
# Register your models here.

@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['email', 'date']
    
@admin.register(MailMessage)
class MailMessageAdmin(admin.ModelAdmin):
    list_display = ['date_sent']
