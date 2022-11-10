from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

# Create your views here.
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'회원 가입이 완료되었습니다'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomeTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer