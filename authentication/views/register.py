from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from authentication.serializers import UserSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer