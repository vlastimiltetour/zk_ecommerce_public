from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.urls import reverse #this is when calling an address by name
from django.db import models
from django.utils import timezone



# Create your models here.
# Each time any DB created, use makemigrations and migrate.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True) #slug field (unique implies the creation of an index)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self): #this is a convention to retrieve the URL for a given ogbject
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE) #one to many relationship, a product belongs to one category and a category contains multiple products
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200) #a slug to build beautiful URLs
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    #cz_price = MoneyField(max_digits=14, decimal_places=0, default_currency='CZK', null=True)
    #eur_price = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR', null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    headline = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']), #the hyphen is to define an index with a descending order!!!
        ]
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __iter__(self):
        return self.name
    

