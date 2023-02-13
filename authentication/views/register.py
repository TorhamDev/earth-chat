from rest_framework.views import APIView
from authentication.serializers import UserSerializer
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

        if request.data["confirm_password"] != request.data["password"]:
            raise ValidationError(
                "Confirm password doesn't match.",
                status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
