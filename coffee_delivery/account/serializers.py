# users/serializers.py
from .models import User # User 모델
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구
from django.utils import timezone


# 회원가입 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.only('email'))], # 이메일에 대한 중복 검증
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password], # 비밀번호에 대한 검증
    )
    phone_number = serializers.CharField(
        write_only=True,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.only('phone_number'))] # 핸드폰 번호 검증
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'phone_number')

    def validate(self, data):
        phone_number = data['phone_number']
        if len(phone_number) != 11:
            raise serializers.ValidationError(
                detail={"detail": "The phone number must be composed of exactly 11 digits"},
                code='phone_number_length')
        elif not phone_number.isdigit():
            raise serializers.ValidationError(
                detail={"detail": "The phone number must consist of numbers only."},
                code='phone_number_in_string')
        return data

    def create(self, validated_data):
        # CREATE 요청에 대해 create 메서드를 오버라이딩하여, 유저를 생성
        user = User.objects.create_user(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return data
    
    def create(self, validated_data):
        email = validated_data['email']
        user = User.objects.filter(email=email).first()
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        return user