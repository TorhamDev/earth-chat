from jwt import decode as jwt_decode
from jwt.exceptions import ExpiredSignatureError, DecodeError
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework import status


def check_user_register_data(request):

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

    return True


def authorization_with_jwt(jwt_token: str):

    print(jwt_token)
    try:
        result = jwt_decode(
            jwt_token,
            key=settings.SECRET_KEY,
            algorithms="HS256",
        )
    except (ExpiredSignatureError, DecodeError):
        return False

    user = User.objects.get(id=result["user_id"])

    return user
