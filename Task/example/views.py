from example.serializers import UserCreateSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User 

# Наборы представлений описывают поведение представлений.
class APIUserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

