from django.contrib.auth.models import User


class EmailAuthBackend:

    @staticmethod
    def authenticate(request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    @staticmethod
    def get_user(user_id):
        try:
            User.objects.get(pk=user_id)

        except User.DoesNotExict:
            return None
