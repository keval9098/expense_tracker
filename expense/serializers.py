from rest_framework import routers, serializers, viewsets
from . models import spent, User


class Spent_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = spent
        fields=['id', 'user_name','spent_on', 'reason', 'amount']


class User_serializer(serializers.ModelSerializer):
    class Meta:

        model= User
        fields=['id', 'email', 'is_superuser']