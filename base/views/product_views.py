from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from base.models import Product
from base.serializers import ProductSerializer
from rest_framework.permissions import IsAdminUser
# password


# Products
@api_view(['Get'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# product by id
@api_view(['Get'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


# Create Product
@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user
    product = Product.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        brand='Sample Brand',
        countInStock=0,
        category='sample Category',
        description=''
    )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


# update Product
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    # get data from frontEnd
    data = request.data
    product = Product.objects.get(_id=pk)
    # get data from front end and update
    product.name = data['name']
    product.price = data['price']
    product.brand = data['brand']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.description = data['description']
    product.save()
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


# delete Product with id
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Product Deleted Success !')
