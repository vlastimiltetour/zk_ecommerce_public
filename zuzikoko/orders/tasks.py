from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from email.mime.text import MIMEText

from django.utils.html import strip_tags
from web.settings import local


from pathlib import Path
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives


# the function for sending an email
#cele task is a function decorated
@shared_task
def hello():
    print("Hello there!") 


@shared_task
def order_created_html(order_id):
    order = Order.objects.get(id=order_id)
    html_content = render_to_string("orders/order/order_confirmed.html",  {'order': order})

    message = EmailMultiAlternatives(
        subject='Your order {order.id} is confirmed.',
        body="mail testing",
        from_email='zuzi@zuzikoko.com',
        to=[order.email]
)

    message.attach_alternative(html_content, "text/html")
    return message.send(fail_silently=False)




# send an test email
#order_created(subject="TEST", text_content=text_message, html_content=html_message, sender=sender, recipient=recipient, image_path=image_path, image_name=image_name)'''

'''

recipient = "v.tetour@gmail.com"
sender = "zuzi@zuzikoko.com" 
image_path = '/Users/vlastimil/Coding_Projects/zk/zuzikoko/shop/static/assets/img/merve_main.jpg'
image_name = Path(image_path).name

subject = "Your order is confirmed"
text_message = f"Email with a nice embedded image {image_name}."

html_message = render_to_string("orders/order/order_confirmation.html")

# the function for sending an email
#cele task is a function decorated
def order_created_html(subject, text_content, html_content=None, sender=sender, recipient=recipient, image_path=None, image_name=None):
    email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sender, to=recipient if isinstance(recipient, list) else [recipient])
    #order = Order.objects.get(id=order_id)
    if all([html_content,image_path,image_name]):
        email.attach_alternative(html_content, "text/html")
        email.content_subtype = 'html'  # set the primary content to be text/html
        email.mixed_subtype = 'related' # it is an important part that ensures embedding of an image 

        with open(image_path, mode='rb') as f:
            image = MIMEImage(f.read())
            email.attach(image)
            image.add_header('Content-ID', f"<{image_name}>")

    email.send()


# send an test email
#order_created(subject="TEST", text_content=text_message, html_content=html_message, sender=sender, recipient=recipient, image_path=image_path, image_name=image_name)'''



@shared_task #cele task is a function decorated
def test(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order non HTML nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'zuzi@zuzikoko.com', [order.email])

    return mail_sent