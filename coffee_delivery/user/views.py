# Create your views here.
import requests
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .serializers import CustomRegisterSerializer, LoginSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import redirect
from my_settings import SOCIALACCOUNT_PROVIDERS, STATE, MAIN_DOMAIN
from user.models import User
from allauth.socialaccount.providers.naver import views as naver_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(request=request)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = JsonResponse(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = TokenObtainPairSerializer.get_token(user) # refresh 토큰 생성
            refresh_token = str(token) # refresh 토큰 문자열화
            access_token = str(token.access_token) # access 토큰 문자열화
            response = JsonResponse(
                {
                    "user": user.id,
                    "message": "login success",
                    "jwt_token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token
                    },
                },
                status=status.HTTP_200_OK
            )
            response.set_cookie("access_token", access_token, httponly=True)
            response.set_cookie("refresh_token", refresh_token, httponly=True)
            return response
        else:
            return JsonResponse(
                {"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

class NaverLoginAPI(APIView):
    def get(self, request, *args, **kwargs):
        client_id = SOCIALACCOUNT_PROVIDERS['naver']['APP']['client_id']
        response_type = "code"
        uri = 'http://127.0.0.1:8000/user/naver/callback'
        state = STATE
        url = "https://nid.naver.com/oauth2.0/authorize"
        return redirect(
            f'{url}?response_type={response_type}&client_id={client_id}&redirect_uri={uri}&state={state}'
        )

class NaverCallbackAPIView(APIView):
    def get(self, request, *args, **kwargs):
        error = request.GET.get('error')
        if error:
            if error == 'access_denied':
                return JsonResponse(
                    data={'message': '필수 항목에 동의하여야 서비스 이용이 가능합니다.'},
                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse(
                    data={'message': f'{error.__str__()}'},
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            grant_type = 'authorization_code'
            client_id = SOCIALACCOUNT_PROVIDERS['naver']['APP']['client_id']
            client_secret = SOCIALACCOUNT_PROVIDERS['naver']['APP']['secret']
            code = request.GET.get('code')
            state = request.GET.get('state')
            parameters = f'grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}&'\
                        f'code={code}&state={state}'
            token_request = requests.get(f"https://nid.naver.com/oauth2.0/token?{parameters}").json()
            access_token = token_request.get("access_token")
            user_info_request = requests.get(
                "https://openapi.naver.com/v1/nid/me",
                headers={"Authorization": f"Bearer {access_token}"})
            if user_info_request.status_code != 200:
                return JsonResponse({"error": "failed to get email."}, status=status.HTTP_400_BAD_REQUEST)
            user_profile = user_info_request.json()['response']
            email = user_profile['email']
            phone_number = user_profile['mobile']
        try:
            user = User.objects.get(email=email)
            data = {'access_token': access_token, 'code': code}
            # accept 에는 token 값이 json 형태로 들어온다({"key"}:"token value")
            # 여기서 오는 key 값은 authtoken_token에 저장된다.
            accept = requests.post(
                f"{MAIN_DOMAIN}/user/naver/login/success", data=data)
            # 만약 token 요청이 제대로 이루어지지 않으면 오류처리
            if accept.status_code != 200:
                return JsonResponse({"error": "Failed to Signin."}, status=accept.status_code)
            return JsonResponse(accept.json(), status=status.HTTP_200_OK)
        except User.DoesNotExist:
            data = {'email': email, 'phone_number': phone_number}
            return JsonResponse(data=data)

class NaverToDjangoLoginView(SocialLoginView):
    adapter_class = naver_views.NaverOAuth2Adapter
    client_class = OAuth2Client

class KakaoLoginAPI(APIView):
    def post(self, request):
        pass