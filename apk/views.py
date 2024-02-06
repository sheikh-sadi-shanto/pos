from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apk.models import CrimeVideos
from apk.serializer import CrimeVideosSerializer

# Create your views here.
class CrimeVideosView(APIView):
    def get(self,request,pk=None):
        queryset=CrimeVideos.objects.all()
        serializers=CrimeVideosSerializer(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers=CrimeVideosSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'created successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)
