from django.shortcuts import render

def hello_world(request):
    return render(request, template_name='index.html')


def iphone(request):
    return render(request,template_name='iphone.html')

from rest_framework.generics import ListAPIView,RetrieveAPIView, DestroyAPIView, RetrieveDestroyAPIView
from .models import UserModel
from .serializers import UserListSerializer, UserRetrieveSerializer

class UserView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserListSerializer

# class UserRetrieveView(RetrieveAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserRetrieveSerializer

# class UserDelete(DestroyAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserRetrieveSerializer

class UserRetrieveDelete(RetrieveDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRetrieveSerializer