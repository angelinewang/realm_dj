from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
# Returns user model that is active in this project. Django has a default built-in user model: Already has a function set up for you
from django.conf import settings
import jwt
User = get_user_model()
# Retrieving our User model in the variable above

class JWTAuthentication(BasicAuthentication):
    def authenticate(self, request):
        # Grabbing the Authorization Header from the Request
        header = request.headers.get('Authorization')
        # Existing if the Header does not exist
        if not header:
            return None
        # Throwing an Error if the Header does not start with the word Bearer
        if not header.startswith('Bearer'):
            raise PermissionDenied(
                {'message': 'Invalid Authorization Header!'})
        # Grabbing the token from the Header by replacing the word 'Bearer' with an empty string, and we end up with just an empty string
        token = header.replace('Bearer', '')

        try:
            # Decode token and fetch associated user
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=payload.get('sub'))
        # Throw an error if the token is invalid
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied({'message': 'Invalid Token'})
        # Throw an error if the User does exist/cannot find user
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'User not found'})
        # Finally, if everything goes well, return a tuple with the user and token elements
        return (user, token)

        # Handy to have a lot of errors written out so you can solve the bug much more easily
