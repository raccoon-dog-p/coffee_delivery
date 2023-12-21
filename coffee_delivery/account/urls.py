from django.urls import path
from .views import RegisterAPIView, UserLoginAPI

urlpatterns =[
    path('sign-up', RegisterAPIView.as_view()),
    path('sign-in', UserLoginAPI.as_view())
    # path('api-auth/', include('rest_framework.urls')),
 ]