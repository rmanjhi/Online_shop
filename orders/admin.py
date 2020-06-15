from django.contrib import admin

from orders import models

admin.site.register(models.UserCheckout)
admin.site.register(models.UserAddress)
admin.site.register(models.Order)