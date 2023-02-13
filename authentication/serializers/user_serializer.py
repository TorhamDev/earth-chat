from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation["password"]

        return representation