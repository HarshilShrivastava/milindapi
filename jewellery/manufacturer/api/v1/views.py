from manufacturer.api.v1.serializer import(
    manufacturerserializer,
    MOrnamentserializer,
    MbucketSerializer,
    RequestListSerializer,
)
from manufacturer.models import(
    Manufacturer,
    MOrnament,
    Mbucket,
    MWIR,
    MWIC
)
from wholeseller.models import(
   Wholeseller
)

from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required 
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
)

class Manufacturerprofile(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_MANUFACTURER==1:
            serializer=manufacturerserializer(data=request.data)
            if serializer.is_valid():
                serializer.save(User=self.request.user)
                context['status']=200
                context['sucess']=True
                context['message']="sucessfully created"
                data=serializer.data
                context['data']=data
                return Response(context)
            else:
                context['status']=400
                context['sucess']=False
                context['message']="not  created"
                data=serializer.errors
                context['data']=data
                return Response(context)
        else:
            context['status']=400
            context['sucess']=False
            context['message']="Unauthorised acess "
            data=serializer.errors
            context['data']=data
            return Response(context)
    def get(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_MANUFACTURER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

        try:
            profile=get_object_or_404(Manufacturer  ,User=request.user)
            print(profile)
        except:
            context['sucess']=False
            context['status']=400
            context['message']="fill the form"
            context['data']=data
            return Response(context)
        serializer=manufacturerserializer(profile)
        context['sucess']=True
        context['status']=200
        context['message']="already exist"
        data=serializer.data
        context['data']=data
        return Response(context)
    
    def put(self,request,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_MANUFACTURER == 1:
            obj=get_object_or_404(Manufacturer,User=request.user)
            serializer = manufacturerserializer(obj,data=request.data)
            if serializer.is_valid():
                serializer.save(User=self.request.user)
                context['status']=200
                context['sucess']=True
                context['message']="sucessfully created"
                data=serializer.data
                context['data']=data
                return Response(context)
            context['sucess']=False
            context['status']=400
            context['message']="fill the form"
            context['data']=data
            return Response(context)
        else:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

class ManufacturerOrnament(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_MANUFACTURER==1:
            serializer=MOrnamentserializer(data=request.data)
            print(request.user)
            obj=get_object_or_404(Manufacturer,User=request.user)
            print(obj)
            if serializer.is_valid():
             #     print(serializer.data)
                serializer.save(Manufacturer=obj)
                context['status']=200
                context['sucess']=True
                context['message']="sucessfully created"
                data=serializer.data
                context['data']=data
                return Response(context)
            else:
                context['status']=400
                context['sucess']=False
                context['message']="not  created"
                data=serializer.errors
                context['data']=data
                return Response(context)
        else:
            context['status']=400
            context['sucess']=False
            context['message']="Unauthorised acess "
            data=serializer.errors
            context['data']=data
            return Response(context)
    def get(self, request,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_MANUFACTURER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

        obj=get_object_or_404(Manufacturer,User=request.user)
        Ornament=MOrnament.objects.filter(Manufacturer=obj)
        print(Ornament)
        context['sucess']=False
        context['status']=400
        context['message']="fill the form"
        context['data']=data
        serializer=MOrnamentserializer(Ornament,many=True)
        context['sucess']=True
        context['status']=200
        context['message']="list"
        data=serializer.data
        context['data']=data
        return Response(context)
    
class ManufacturerOrnamentDetail(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def put(self,request,pk,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_MANUFACTURER == 1:
            obj=get_object_or_404(MOrnament,pk=pk)
            obj1=get_object_or_404(Manufacturer,User=request.user)
            serializer = MOrnamentserializer(obj,data=request.data)
            if serializer.is_valid():
                serializer.save(Manufacturer=obj1)
                context['status']=200
                context['sucess']=True
                context['message']="sucessfully created"
                data=serializer.data
                context['data']=data
                return Response(context)
            context['sucess']=False
            context['status']=400
            context['message']="fill the form"
            context['data']=data
            return Response(context)
        else:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)
    def get(self,request,pk,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_MANUFACTURER == 1:
            obj=get_object_or_404(MOrnament,pk=pk)
            serializer = MOrnamentserializer(obj)
            data=serializer.data
            context['sucess']=True
            context['status']=200
            context['message']="fill the form"
            context['data']=data
            return Response(context)
        else:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

#add object in bucket
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def add_in_bucket(request,id):
    context={}
    data={}
    obj=get_object_or_404(Manufacturer,User=request.user)
    Ornament=get_object_or_404(MOrnament,pk=id)
    print(object)
    print()
    try:
        obj1=Mbucket.objects.create(FROM=obj,ORNAMENT=Ornament)
    except:
        context['sucess']=False
        context['status']=400
        context['message']=" can't add to bucket"
        context['data']=data
        return Response(context)
    context['sucess']=True
    context['status']=200
    context['message']="fill the form"
    context['data']=data
    return Response(context)
#delete item from bucket
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def deletefrombucket(request,pk):
    context={}
    data={}
    try:
        obj=get_object_or_404(Mbucket,pk=pk)
        obj.delete()
    except:
        context['sucess']=False
        context['status']=400
        context['message']="not deleted"
        context['data']=data
        return Response(context)
    context['sucess']=True
    context['status']=200
    context['message']="sucessfully deleted"
    context['data']=data
    return Response(context)

# all item in bucket
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def list_of_all(request):
    obj=get_object_or_404(Manufacturer,User=request.user)
    context={}
    data={}
    qs=Mbucket.objects.all().filter(FROM=obj)
    print(qs)
    srializer=MbucketSerializer(qs,many=True)
    data=srializer.data
    context['sucess']=True
    context['status']=200
    context['count']=qs.count()
    context['message']="sucessfully get"
    context['data']=data
    return Response(context)

# add friend request to wholseller
@api_view(['POST', ])
#@permission_classes((IsAuthenticated, ))
def add(request,wholseller,manufacturer,message):
    context={}
    data={}
    wholseller=get_object_or_404(Wholeseller,pk=wholseller)
    manufacturer=get_object_or_404(Manufacturer,pk=manufacturer)
    try:
        obj=MWIR.objects.get(Manufacturer=manufacturer,Wholeseller=wholseller,message=message)
    except:
        context['sucess']=True
        obj=MWIR.objects.create(Manufacturer=manufacturer,Wholeseller=wholseller,message=message)
        context['status']=200
        context['message']="sent friend request"
        context['data']=data
        return Response(context)
    context['sucess']=False
    context['status']=401
    context['message']=" can't create already a send a request"
    context['data']=data
    return Response(context)

# list friend request to wholseller
@api_view(['GET',])
def list_of_sent(request):
    manufacturer=get_object_or_404(Manufacturer,User=request.user)
    qs=MWIR.objects.filter(Manufacturer=manufacturer)
    context={}
    data={}
    dat=RequestListSerializer(qs,many=True)
    data=dat.data
    
    context['sucess']=True
    context['status']=200
    context['message']="list"
    context['data']=data
    return Response(context)


# delete friend request to wholseller
@api_view(['DELETE',])
def deleterequest(request,id):
    context={}
    data={}
    try:
        obj=MWIR.objects.get(pk=id)
    except:
        context['sucess']=False
        context['status']=400
        context['message']="not found"
        context['data']=data
        return Response(context)
    obj.delete()
    context['sucess']=True
    context['status']=200
    context['message']="sucessfully deleted"
    context['data']=data
    return Response(context)


@api_view(['POST',])
def ConfirmFriendrequestMWI(request,id):
    context={}
    data={}
    try:
        obj=get_object_or_404(MWIR,pk=id)
    except:
        context['sucess']=False
        context['status']=400
        context['message']="no request exist"
        context['data']=data
        return Response(context)
    manufacturer=obj.Manufacturer
    wholeseller=obj.Wholeseller
    try:
        obj2=MWIC.objects.get(Manufacturer=manufacturer,Wholeseller=wholeseller)
    except:

        try:
            obj1=MWIC.objects.create(Manufacturer=manufacturer,Wholeseller=wholeseller)
        except:
            context['sucess']=False
            context['status']=400
            context['message']="can't add friend"
            context['data']=data
            return Response(context)
        context['sucess']=True
        context['status']=200
        context['message']="sucessfully you are friend"
        context['data']=data
        return Response(context)
    context['sucess']=False
    context['status']=400
    context['message']="already a friend"
    context['data']=data
    obj.delete()
    return Response(context)
    
@api_view(['POST',])
def removefriendMWI(request,id):
    context={}
    data={}
    try:
        obj=get_object_or_404(MWIC,pk=id)
        obj.delete()
    except:
        context['sucess']=False
        context['status']=400
        context['message']="can't remove friend"
        context['data']=data
        return Response(context)
    context['sucess']=True
    context['status']=200
    context['message']="Sucessfuly deleted"
    context['data']=data
    return Response(context)