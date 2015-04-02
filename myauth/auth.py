# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from webapi.models import Husers

class MyCustomBackend: 
    def authenticate(self, username=None, password=None):
        try:
            user = Husers.objects.get(username=username)
        except Husers.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                try:
                    django_user = User.objects.get(username=user.username)
                except User.DoesNotExist:
                    #当在django中找不到此用户，便创建这个用户
                    django_user = User(username=user.username,password=user.password)
                    django_user.is_staff = True
                    django_user.save()
                return django_user
            else:
                return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None