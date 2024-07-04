from django.contrib import admin

from blog.models import Product, Image, Attribute

# Register your models here.


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Attribute)
