from django.conf import settings
from api.models import User

class CustomAuthentication(object):

    def authenticate(self, request, username=None):

        
        try:
            user_model = settings.AUTH_USER_MODEL
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        else: 
            return user

    def get_user(self, username):

        try:
            user_model = settings.AUTH_USER_MODEL
            user = user_model.objects.get(username=username)
        except User.DoesNotExist:
            return None
