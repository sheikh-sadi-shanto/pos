from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apk.models import CrimeVideos
from apk.serializer import CrimeVideosSerializer

# Create your views here.
class CrimeVideosView(APIView):
    def get(self,request):
        queryset=CrimeVideos.objects.all()
        serializers=CrimeVideosSerializer(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers=CrimeVideosSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'post successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)


class CrimeVideosViewitem(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            queryset=CrimeVideos.objects.filter(id=pk)
            serializers=CrimeVideosSerializer(queryset,many=True)
            return Response(serializers.data)
    
    def put(self,request,pk=None):
            get_video_query=CrimeVideos.objects.filter(id=pk)
            serializer=CrimeVideosSerializer(get_video_query,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'full data update'})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None):
        get_video_query=CrimeVideos.objects.filter(id=pk)
        serializer=CrimeVideosSerializer(get_video_query,data=request.data,Partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        que=CrimeVideos.objects.filter(id=pk)
        que.delete()
        return Response({'msg':'deleted successfully'})
