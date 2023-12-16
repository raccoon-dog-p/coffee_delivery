from django.urls import path
from .views import CoffeeView, CoffeeBeanView

urlpatterns = [
    path('coffee', CoffeeView.as_view()),
    path('beans', CoffeeBeanView.as_view())
]
