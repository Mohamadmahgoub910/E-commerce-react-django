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


# delete Product with id
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Product Deleted Success !')
