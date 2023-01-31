from modeltranslation.translator import register, translator, TranslationOptions
from .models import Product, Category



@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'slug')



@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')
