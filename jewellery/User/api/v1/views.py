from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import UpdateAPIView

from django.contrib.auth import (
    authenticate,
    get_user_model,
)

from User.api.v1.serializers import (
    RegistrationSerializer,
    UserLoginSerializers,
    ChangePasswordSerializer,
)

User = get_user_model()

def validate_email(email):
    user = None
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    if user != None:
        return email

@api_view(['POST', ])
@permission_classes([AllowAny,])
@authentication_classes([])
def registration_view(request):
    if request.method == 'POST':
        data = {}
        context={}

        email = request.data.get('email', '0')
        if validate_email(email) != None:
            context['sucess'] = False
            context['response'] = status.HTTP_403_FORBIDDEN
            context['error_message'] = 'That email is already in use.'
            context['data']=data
            return Response(context)

        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            context['sucess'] = True
            context['message'] = 'Sucessfully registered'
            context['response'] = status.HTTP_201_CREATED
            data['email'] = user.email
            data['username'] = user.username
            data['IS_MANUFACTURER'] = user.IS_MANUFACTURER
            data['IS_DESIGNER']=user.IS_DESIGNER
            data['IS_WHOLESELLER']=user.IS_WHOLESELLER
            data['IS_RETAILER']=user.IS_RETAILER
            data['IS_CITIZEN']=user.IS_CITIZEN
        else:
            context['sucess'] = False
            context['message'] = str(serializer.errors['username'][0])
            context['response'] = status.HTTP_401_UNAUTHORIZED
            data = serializer.errors
            context['errror']=data
        context['data']=data


    return Response(context)

@api_view(['POST', ])
@permission_classes((AllowAny,))
def login_view(request):
    if request.method == 'POST':
        serializer = UserLoginSerializers(data=request.data)
        data={}
        context={}
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            account=authenticate(username=username ,password=password)
            if account:
                try:
                    token = Token.objects.get(user=account)
                except Token.DoesNotExist:
                    token = Token.objects.create(user=account)
                context['status']=200
                context['sucess']=True
                context['message']="Sucessfully Created"
                
                data['token'] = token.key
                data['IS_MANUFACTURER']=account.IS_MANUFACTURER
                data['IS_DESIGNER']=account.IS_DESIGNER
                data['IS_WHOLESELLER']=account.IS_WHOLESELLER
                data['IS_RETAILER']=account.IS_RETAILER
                data['IS_CITIZEN']=account.IS_CITIZEN
                context['data']=data
                return Response(context)
            else:
                context['status']= 400
                context['sucess'] = False
                context['message'] = 'Invalid credentials'
                context['data']=data
                return Response(context)
        else:
            
            return Response(context)

class ChangePasswordView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    model = User
    authentication_classes = (TokenAuthentication, )

    def get_object(self, queryset = None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        data={}
        context={}
        def get_object(self, queryset = None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get('old_password')):
                context['success'] = "False"
                context['message'] = 'Invalid old password'
                context['status'] = status.HTTP_403_FORBIDDEN
                context['data']=data
                return Response(context)

            # confirm the new password match
            new_password = serializer.data.get("new_password")
            confirm_new_password = serializer.data.get('confirm_new_password')
            if new_password != confirm_new_password:
                context['success'] = "False"
                context['message'] = 'password didnot match'
                context['status'] = status.HTTP_403_FORBIDDEN
                context['data']=data
                return Response(context)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            context['success'] = "True"
            context['message'] = 'password changed sucessfully'
            context['status'] = status.HTTP_200_OK
            context['data']=data
            return Response(context)
        context['success'] = "False"
        context['message'] = serializer.errors
        context['status']=status.HTTP_400_BAD_REQUEST
        context['data']=data
        return Response(context)