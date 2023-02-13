from rest_framework.views import APIView
from authentication.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status


class RegisterView(APIView):

    def post(self, request):

        if "confirm_password" not in request.data:
            raise ValidationError(
                "You forgot confirm_password field.",
                status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.data["confirm_password"] != request.data["password"]:
            raise ValidationError(
                "Confirm password doesn't match.",
                status.HTTP_400_BAD_REQUEST,
            )

        # Create user manualy
        validation_data = serializer.validated_data

        user = User(
            username=validation_data.get("username"),
            email=validation_data.get("email")
        )

        user.set_password(validation_data.get("password"))

        user.save()

        return Response(serializer.data)
