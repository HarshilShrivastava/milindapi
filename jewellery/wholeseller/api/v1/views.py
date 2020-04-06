from wholeseller.models import (
    Wholeseller,
    WOrnament,
    Wbucket,
    WRIC,
    WRI
)
from wholeseller.api.v1.serializers import(
    WholesellerSerializer,
    WholesellerOrnamentSerializer,
    WbucketSerializer,
    RequestListSerializer,
    WholesellerRetailerrequestserializer,
)
from manufacturer.models import(
    MWIR,
    Manufacturer
)

from retailer.models import(
    retailer
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

class wholesellerprofile(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_WHOLESELLER==1:
            serializer=WholesellerSerializer(data=request.data)
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
        if request.user.IS_WHOLESELLER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

        try:
            profile=get_object_or_404(Wholeseller,User=request.user)
        except:
            context['sucess']=False
            context['status']=400
            context['message']="fill the form"
            context['data']=data
            return Response(context)
        serializer=WholesellerSerializer(profile)
        context['sucess']=True
        context['status']=200
        context['message']="already exist"
        data=serializer.data
        context['data']=data
        return Response(context)
    
    def put(self,request,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_WHOLESELLER == 1:
            obj=get_object_or_404(Wholeseller,User=request.user)
            serializer = WholesellerSerializer(obj,data=request.data)
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


class WholesellerOrnament(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_WHOLESELLER==1:
            serializer=WholesellerOrnamentSerializer(data=request.data)
            obj=get_object_or_404(Wholeseller,User=request.user)
            if serializer.is_valid():
             #     print(serializer.data)
                serializer.save(Wholeseller=obj)
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
        if request.user.IS_WHOLESELLER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

        obj=get_object_or_404(Wholeseller,User=request.user)
        Ornament=WOrnament.objects.filter(Wholeseller=obj)
        print(Ornament)
        context['sucess']=False
        context['status']=400
        context['message']="fill the form"
        context['data']=data
        serializer=WholesellerOrnamentSerializer(Ornament,many=True)
        context['sucess']=True
        context['status']=200
        context['message']="list"
        data=serializer.data
        context['data']=data
        return Response(context)
    
class WholeSellerOrnamentDetail(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def put(self,request,pk,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_WHOLESELLER == 1:
            obj=get_object_or_404(WOrnament,pk=pk)
            obj1=get_object_or_404(Wholeseller,User=request.user)
            serializer = WholesellerOrnamentSerializer(obj,data=request.data)
            if serializer.is_valid():
                serializer.save(Wholeseller=obj1)
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
        if request.user.IS_WHOLESELLER == 1:
            obj=get_object_or_404(WOrnament,pk=pk)
            serializer = WholesellerOrnamentSerializer(obj)
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
    obj=get_object_or_404(wholeseller,User=request.user)
    Ornament=get_object_or_404(MOrnament,pk=id)
    print(object)
    print()
    try:
        obj1=Wbucket.objects.create(FROM=obj,ORNAMENT=Ornament)
    except:
        context['sucess']=False
        context['status']=400
        context['message']=" can't add to bucket"
        context['data']=data
        return Response(context)
    context['sucess']=True
    context['status']=200
    context['message']="sucessfully added"
    context['data']=data
    return Response(context)
#delete item from bucket
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def deletefrombucket(request,pk):
    context={}
    data={}
    try:
        obj=get_object_or_404(Wbucket,pk=pk)
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
    obj=get_object_or_404(Wholeseller,User=request.user)
    context={}
    data={}
    qs=Wbucket.objects.all().filter(FROM=obj)
    print(qs)
    srializer=WbucketSerializer(qs,many=True)
    data=srializer.data
    context['sucess']=True
    context['status']=200
    context['count']=qs.count()
    context['message']="sucessfully get"
    context['data']=data
    return Response(context)

# list friend request to manufacturer
@api_view(['POST', ])
#@permission_classes((IsAuthenticated, ))
def add_friendM(request,wholseller,manufacturer,message):
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



@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def list_of_sent(request):
    manufacturer=get_object_or_404(Wholeseller,User=request.user)
    qs=MWIR.objects.filter(Wholeseller=manufacturer)
    context={}
    data={}
    dat=RequestListSerializer(qs,many=True)
    data=dat.data
    context['sucess']=True
    context['status']=200
    context['message']="list"
    context['data']=data
    return Response(context)

@api_view(['DELETE',])
@permission_classes((IsAuthenticated, ))
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
    manufacturer=get_object_or_404(Wholeseller,User=request.user)
    qs=WRI.objects.filter(Wholeseller1=manufacturer)
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


@api_view(['POST',])
def ConfirmFriendrequestWRI(request,id):
    context={}
    data={}
    try:
        obj=get_object_or_404(WRI,pk=id)
    except:
        context['sucess']=False
        context['status']=400
        context['message']="no request exist"
        context['data']=data
        return Response(context)
    manufacturer=obj.Manufacturer
    wholeseller=obj.Wholeseller
    try:
        obj2=WRI.objects.get(Manufacturer=manufacturer,Wholeseller=wholeseller)
    except:

        try:
            obj1=WRIC.objects.create(Manufacturer=manufacturer,Wholeseller=wholeseller)
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
def removefriendWRI(request,id):
    context={}
    data={}
    try:
        obj=get_object_or_404(WRIC,pk=id)
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