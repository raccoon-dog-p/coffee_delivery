from .serializers import CoffeeSerializer, CoffeeBeanSerializer
from .models import Coffee, CoffeeBean
from rest_framework import generics
# Create your views here.

class CoffeeView(generics.CreateAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer


class CoffeeBeanView(generics.CreateAPIView):
    queryset = CoffeeBean.objects.all()
    serializer_class = CoffeeBeanSerializer

