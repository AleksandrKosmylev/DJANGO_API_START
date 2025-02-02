from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductDeteilAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #looku_field = 'pk'

