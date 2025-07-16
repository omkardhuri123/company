from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = {'inventory_list':['Mango','Salad','Dal'],
               'greeting':'THANKS FOR GIVING TO ME'}

    return render(request,'home.html',context)

class AboutPageView(TemplateView):
    template_name ='about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_of_company'] ='MAHINDRA AND MAHINDRA'
        context['address_of_company']='123 a/p manglore'
        return context
