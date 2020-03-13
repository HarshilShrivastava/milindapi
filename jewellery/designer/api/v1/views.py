from designer.api.v1.serializer import(
    designerserializer
)
from designer.models import(
    designer
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

class Designerrprofile(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        context={}
        data={}
        if request.user.IS_DESIGNER==1:
            serializer=designerserializer(data=request.data)
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
        if request.user.IS_DESIGNER == 0:
            context['sucess']=False
            context['status']=400
            context['message']="Unauthorised acess"
            context['data']=data
            return Response(context)

        try:
            profile=get_object_or_404(designer  ,User=request.user)
            print(profile)
        except:
            context['sucess']=False
            context['status']=400
            context['message']="fill the form"
            context['data']=data
            return Response(context)
        serializer=designerserializer(profile)
        context['sucess']=True
        context['status']=200
        context['message']="already exist"
        data=serializer.data
        context['data']=data
        return Response(context)
    
    def put(self,request,*args, **kwargs):
        context={}
        data={}
        if request.user.IS_DESIGNER== 1:
            obj=get_object_or_404(designer,User=request.user)
            serializer = designerserializer(obj,data=request.data)
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

