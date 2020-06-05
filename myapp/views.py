# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer
from .models import Customer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer    

def get_customer_list(request):
    customer_list = Customer.objects.all()
    context = {
        'customer_list': customer_list
    }
    return render(request, 'index.html', context=context)