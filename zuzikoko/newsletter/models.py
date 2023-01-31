from django.db import models
from django.utils import timezone


# Create your models here.
class Subscribers(models.Model):
    email = models.EmailField(max_length=100, null=True)
    date = models.DateTimeField('Date created', auto_now_add=True)

    class Meta:
        ordering = ['date']
        indexes = [
            models.Index(fields=['email'])
        ]

    def __str__(self):
        return self.email


    
class MailMessage(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField(null=True)
    date_sent = models.DateTimeField('Date sent', default=timezone.now)

    class Meta:
        ordering = ['date_sent']
        indexes = [
            models.Index(fields=['date_sent'])
        ]

    def __str__(self):
        return self.title