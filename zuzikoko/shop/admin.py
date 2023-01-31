from django.contrib import admin
from .models import Category, Product
from .translations import Category, Product
from modeltranslation.admin import TranslationAdmin
from modeltranslation.models import *
from modeltranslation.utils import (get_translation_fields, build_localized_fieldname, build_css_class)
from djmoney.money import Money


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)} #prepopulated fields attribute to specify fields where value is automatcally set

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'headline']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'headline']
    prepopulated_fields = {'slug':('name', )}




