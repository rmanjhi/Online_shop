from django.views.generic import TemplateView
from Products.models import Product
from django.shortcuts import render

class homeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        prod = Product.objects.all()
        args = {'prod': prod}
        return render(request, self.template_name, args)

