from .models import User
from rest_framework import generics, permissions
from .serializer import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
import jwt
import datetime

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        #password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not found")

#if not user.check_password(password):
#raise AuthenticationFailed("Incorrect password")

        else:
            payload = {
                'id':user.id,
                'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat':datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')
            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt':token
            }
            return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Not authenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Not authenticated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserRegistrationSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'Logout Successful'
        }
        return response

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self, request):
        qs = super().get_queryset()
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Not authenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Not authenticated')

        if qs is not None:
            return qs.filter(id=payload['id']).first()

        else:
            return User.objects.none()