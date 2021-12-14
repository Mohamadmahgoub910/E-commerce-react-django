from django.shortcuts import render
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['Get'])
def getProducts(request):
    return Response(products)

@api_view(['Get'])
def getProduct(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
    return Response(product)