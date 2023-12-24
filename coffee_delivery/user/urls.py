from django.urls import path
from .views import RegisterAPIView, UserLoginAPI, NaverLoginAPI, NaverCallbackAPIView, NaverToDjangoLoginView

urlpatterns =[
    path('sign-up', RegisterAPIView.as_view()),
    path('sign-in', UserLoginAPI.as_view()),
    path('naver', NaverLoginAPI.as_view()),
    path('naver/callback', NaverCallbackAPIView.as_view()),
    path('naver/login/success', NaverToDjangoLoginView.as_view())
    # path('api-auth/', include('rest_framework.urls')),
 ]