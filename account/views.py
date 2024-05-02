from django.shortcuts import render
from rest_framework.response import Response 
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

User = get_user_model()


from .serializers import RegisterSerializer

class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        data = request.data
        serializers = RegisterSerializer(data=data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
        return Response('You Registered')
    
class ActivateView(APIView):  
    def get(self, request, email, activation_code): 
        user = user.objects.filter(email=email, activation_code=activation_code).first()
        if not user: 
            return Response('User not found', status=404)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('You have activated!', 200)



