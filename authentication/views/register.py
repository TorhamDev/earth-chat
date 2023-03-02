from rest_framework.views import APIView
from authentication.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from authentication.utils.user_authorization import check_user_register_data


class RegisterView(APIView):

    def post(self, request):

        check_user_register_data(request)

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create user manualy
        validation_data = serializer.validated_data

        user = User(
            username=validation_data.get("username"),
            email=validation_data.get("email")
        )

        user.set_password(validation_data.get("password"))

        user.save()

        return Response(serializer.data)
