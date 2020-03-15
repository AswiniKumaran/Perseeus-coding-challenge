from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class EmailListView(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class EmailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()

class PhoneNumberListView(generics.ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class PhoneNumberView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhoneNumberSerializer
    queryset = PhoneNumber.objects.all()
