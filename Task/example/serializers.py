from rest_framework import serializers
from django.contrib.auth.models import User


# Сериализаторы описывают представление данных.
class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [ 'url', 'username', 'email', 'is_active', 'is_staff','is_superuser',]

        def create(self, validate_data):

          user = User(
            username = validate_data['username'],
            lastname = validate_data['lastname'],
            middlename = validate_data['middlename'],
            phone = validate_data['phone']

         )

          return user


