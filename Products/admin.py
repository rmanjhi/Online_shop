from django.contrib import admin
from . import models

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageInline,)
    list_display = ('__unicode__', 'price')
    class Meta:
        model = models.Product



# Register your models here.
admin.site.register(models.Product, ProductAdmin)