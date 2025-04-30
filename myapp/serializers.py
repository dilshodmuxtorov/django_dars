from rest_framework.serializers import ModelSerializer
from .models import UserModel


class UserListSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','name','email']

class  UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"