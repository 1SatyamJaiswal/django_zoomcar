from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        name = User
        fields = ['id','username', 'email', 'password']
        
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'email')