from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import authentication
from rest_framework import exceptions

class PostTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token_key = request.data.get('X_Auth_Token')
       
        if not token_key:
            return None

        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such token')

        return (token.user, None)