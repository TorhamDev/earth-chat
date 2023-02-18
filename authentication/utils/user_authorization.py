from jwt import decode as jwt_decode
from jwt.exceptions import ExpiredSignatureError, DecodeError
from django.conf import settings
from django.contrib.auth.models import User



def authorization_with_jwt(jwt_token: str):

    print(jwt_token)
    try:
        result = jwt_decode(
            jwt_token,
            key=settings.SECRET_KEY,
            algorithms="HS256",
        )
    except (ExpiredSignatureError, DecodeError) as e:
        print(e)
        return False

    user = User.objects.get(id=result["user_id"])
    
    return user
    
