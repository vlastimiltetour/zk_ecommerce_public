from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from .models import OrderItem, Order
from .forms import OrderCreateForm
from .tasks import order_created_html
from cart.cart import Cart
from django.core.mail import EmailMultiAlternatives

from pathlib import Path
from email.mime.image import MIMEImage

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            
            order_created_html.delay(order.id)

            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
        
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=19)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    #this line  base_url=request.build_absolute_uri() is to add image to the rendering
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT / 'css/pdf.css')])
            
    return response


def order_confirmed(request):
    order = get_object_or_404(Order, id=172)

    return render(request, 'orders/order/order_confirmed.html',{'order':order})

def about(request):
    return render(request, 'shop/about.html', {})

#order_created_html(subject=subject,text_content=text_message, html_content=html_message, sender=sender, recipient=recipient, image_path=image_path, image_name=image_name)