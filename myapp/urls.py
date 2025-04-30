from django.urls import path
from .views import *
urlpatterns = [
    path('',hello_world),
    path('iphone/', iphone),
    path('userapi/',UserView.as_view()),
    # path('userapi/<int:pk>/',UserRetrieveView.as_view()),  
    # path('delete/<int:pk>/',UserDelete.as_view())
    path('userapi/<int:pk>/',UserRetrieveDelete.as_view())
]