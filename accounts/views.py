from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import update_last_login
# Create your views here.
class RegistrationView(CreateAPIView):
    serializer_class=RegistrationSerializer
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            serializer = RegistrationSerializer(data = request.data)
            data={}
            if serializer.is_valid():
                my_user = serializer.save()
                token = Token.objects.get(user = my_user).key
                data['token']=token
                data['username']=my_user.username
            else:
                data=serializer.errors
            return Response(data)

class LoginView(CreateAPIView):
    serializer_class=LoginSerializer
    def post(self,request):
        if request.method == 'POST':
            serializer = LoginSerializer(data = request.data)
            serializer.is_valid(raise_exception = True)
            user = MyUser.objects.get(username = serializer.data['username'])
            token = Token.objects.get(user = user).key
            update_last_login(None, user) 
            data = {}
            data['token'] = token
            data['user_id']=user.user_id
            data['username']=user.username
            return Response(data, status = status.HTTP_200_OK)
