from retailer.models import (
    retailer,
    ROrnament,
    Rbucket
)
from retailer.api.v1.serializers import(
    retailerserializer,
    ROrnamentserializer,
    BucketSerializer,
    WholesellerRetailerrequestserializer
)
from wholeseller.models import(
    WRI,
    Wholeseller,
)


from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required 
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
)

class Retailerprofile(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_RETAILER==1:
            serializer=retailerserializer(data=request.data)
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
        if request.user.IS_RETAILER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

        try:
            profile=get_object_or_404(retailer,User=request.user)
            print(profile)
        except:
            context['sucess']=False
            context['status']=400
            context['message']="fill the form"
            context['data']=data
            return Response(context)
        serializer=retailerserializer(profile)
        context['sucess']=True
        context['status']=200
        context['message']="already exist"
        data=serializer.data
        context['data']=data
        return Response(context)
    
    def put(self,request,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_RETAILER == 1:
            obj=get_object_or_404(retailer,User=request.user)
            serializer = retailerserializer(obj,data=request.data)
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

class RetailerOrnament(APIView):


    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_RETAILER==1:
            serializer=ROrnamentserializer(data=request.data)
            print(request.user)
            obj=get_object_or_404(retailer,User=request.user)
            print(obj)
            if serializer.is_valid():
                serializer.save(retailer=obj)
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
           # data=serializer.errors
            context['data']=data
            return Response(context)
    def get(self, request,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_RETAILER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

        obj=get_object_or_404(retailer,User=request.user)
        Ornament=ROrnament.objects.filter(retailer=obj)
        context['sucess']=False
        context['status']=400
        context['message']="fill the form"
        context['data']=data
        serializer=ROrnamentserializer(Ornament,many=True)
        context['sucess']=True
        context['status']=200
        context['message']="list"
        data=serializer.data
        context['data']=data
        return Response(context)

class ReatailerOrnamentDetail(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def put(self,request,pk,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_RETAILER == 1:
            obj=get_object_or_404(ROrnament,pk=pk)
            obj1=get_object_or_404(retailer,User=request.user)
            serializer = ROrnamentserializer(obj,data=request.data)
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
        if request.user.IS_RETAILER == 1:
            obj=get_object_or_404(ROrnament,pk=pk)
            serializer = ROrnamentserializer(obj)
            data=serializer.data
            context['sucess']=True
            context['status']=200
            context['message']="Sucessfull get"
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
    obj=get_object_or_404(retailer,User=request.user)
    Ornament=get_object_or_404(ROrnament,pk=id)
    try:
        obj1=Rbucket.objects.create(FROM=obj,ORNAMENT=Ornament)
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

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def deletefrombucket(request,pk):
    context={}
    data={}
    try:
        obj=get_object_or_404(Rbucket,pk=pk)
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
def allfrombucket(request):
    obj=get_object_or_404(retailer,User=request.user)
    context={}
    data={}
    qs=Rbucket.objects.all().filter(FROM=obj)
    print(qs)
    srializer=BucketSerializer(qs,many=True)
    data=srializer.data
    context['sucess']=True
    context['status']=200
    context['count']=qs.count()
    context['message']="sucessfully get"
    context['data']=data
    return Response(context)


#add request in WRI
@api_view(['POST',])
@permission_classes((IsAuthenticated, ))
def add_friendW(request,wholseller,retailr,message):
    context={}
    data={}
    wholseller=get_object_or_404(Wholeseller,pk=wholseller)
    retailerobj=get_object_or_404(retailer,pk=retailr)
    try:
        obj=WRI.objects.get(retailer=retailerobj,Wholeseller1=wholseller,message=message)
    except:
        context['sucess']=True
        obj=WRI.objects.create(retailer=retailerobj,Wholeseller1=wholseller,message=message)
        context['status']=200
        context['message']="sent friend request"
        context['data']=data
        return Response(context)
    context['sucess']=False
    context['status']=401
    context['message']=" can't create already a send a request"
    context['data']=data
    return Response(context)


#list of pending in WRI
@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def list_of_sentW(request):
    userobj=get_object_or_404(retailer,User=request.user)
    qs=WRI.objects.filter(retailer=userobj)
    context={}
    data={}
    dat=WholesellerRetailerrequestserializer(qs,many=True)
    data=dat.data
    context['sucess']=True
    context['status']=200
    context['message']="list"
    context['data']=data
    return Response(context)
#delete request in WRI
@api_view(['DELETE',])
@permission_classes((IsAuthenticated, ))
def deleterequestW(request,id):
    context={}
    data={}
    try:
        obj=WRI.objects.get(pk=id)
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
