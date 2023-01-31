from django.contrib import admin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe
import csv, datetime
from  django.http import HttpResponse
from django.urls import reverse



def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename = {opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not \
        field.many_to_many and not field.one_to_many]

    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d%m%Y')
            data_row.append(value)
        writer.writerow(data_row)
        return response 

export_to_csv.short_description = 'Export to CSV'


def order_payment(obj):
    url = obj.get_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html) #to avoid auto_escaping; Avoid using mark_safe on input that has come from the user to avoid Cross-Site Scripting (XSS). XSS enables attackers to inject client-side scripts into web content viewed by other user“
    return ''

order_payment.short_description = "Stripe payment"  #this sets the name of the column

#this function didn't work, I had to solve this issue by manually updating the libraries, cause MacM1: https://stackoverflow.com/questions/69097224/gobject-2-0-0-not-able-to-load-on-macbook
def order_pdf(obj):
    url = reverse('orders:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')

order_pdf.short_description = 'Invoice' #this sets the name of the column


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


#this is to display the pdf
def order_detail(obj):
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', order_payment, 'created', 'updated', order_detail, order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inline = [OrderItemInline]
    actions = [export_to_csv]
    

