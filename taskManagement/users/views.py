from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer
from .models import User

class UserModelView(ModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer

#vamos a autenticar a los usuarios
#APIView cuando queremos tener el control de la solicitud
class AuthenticateView(APIView):
    def post(self, request):
        user_request= UserLoginSerializer(data=request.data)
#is_valid() solo se usa para serializadores
        if not user_request.is_valid():
            return Response({ "message": 'El email y/o contraseña son invalido(s)' })
        
        user= User.objects.get(email=user_request.data['email'])
        if not user:
            return Response({"message": 'El email es incorrecto'})
        
        password= User.objects.get(password=user_request.data["password"])
        if not password:
            return Response({"message": "La contraseña es incorrecta"})

