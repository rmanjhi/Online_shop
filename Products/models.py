from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=(self.id,))

    def get_image_url(self):
        img = self.productimage_set.first()
        return img.image.url if img else img

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='products/', null=True)

    def __unicode__(self):
        return self.product.title