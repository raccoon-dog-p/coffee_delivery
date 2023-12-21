from django.urls import path
from .views import RegisterAPIView

urlpatterns =[
    path('sign-up', RegisterAPIView.as_view()),
    # path('api-auth/', include('rest_framework.urls')),
 ]