from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from video.models import *
from video.serializer import *
import platform

# Create your views here.
class CrimeVideosView(APIView):
    def get(self,request,pk=None):
        if pk:
            video = CrimeVideos.objects.get(pk=pk)
            # Get the device's unique identifier name (e.g.,device unique information)
            device_identifier2 = str(platform.uname())
            print(device_identifier2)
                
            if device_identifier2 not in video.views_by_devices:
                video.view_count += 1
                video.views_by_devices.append(device_identifier2)
                video.save()

        if pk is not None:
            queryset=CrimeVideos.objects.filter(id=pk)
            serializers=CrimeVideosSerializer(queryset,many=True)
            return Response(serializers.data)
        queryset=CrimeVideos.objects.all()
        serializers=CrimeVideosSerializer(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers=CrimeVideosSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'post successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)
    

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


class CommentViewitem(APIView):
    def get(self,request,video_id=None):
        try:
            video=CrimeVideos.objects.get(id=video_id)
        except:
            raise NotFound('video not found')
        comment=Comment.objects.filter(video=video)
        serializers=CommentSerializer(comment,many=True)
        return Response(serializers.data)
    
    def post(self,request,video_id):
        try:
            video=CrimeVideos.objects.get(id=video_id)
        except:
            raise NotFound('video not found')
        
        serializers=CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(video=video)
            return Response({'msg':'post successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)
    


#############Entertainment#############

class EntertainmentVideosView(APIView):
    def get(self,request,pk=None):
        if pk:
            video = EntertainmentVideos.objects.get(pk=pk)
            # Get the device's unique identifier name (device unique information)
            device_identifier2 = str(platform.uname())
            print(device_identifier2)
                
            if device_identifier2 not in video.views_by_devices:
                video.view_count += 1
                video.views_by_devices.append(device_identifier2)
                video.save()

        if pk is not None:
            queryset=EntertainmentVideos.objects.filter(id=pk)
            serializers=EntertainmentSerializer(queryset,many=True)
            return Response(serializers.data)
        queryset=EntertainmentVideos.objects.all()
        serializers=EntertainmentSerializer(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers=EntertainmentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'post successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)
    

    def put(self,request,pk=None):
            get_video_query=EntertainmentVideos.objects.filter(id=pk)
            serializer=EntertainmentSerializer(get_video_query,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'full data update'})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,pk=None):
        get_video_query=EntertainmentVideos.objects.filter(id=pk)
        serializer=EntertainmentSerializer(get_video_query,data=request.data,Partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        que=EntertainmentVideos.objects.filter(id=pk)
        que.delete()
        return Response({'msg':'deleted successfully'})


class EntertainmentCommentViewitem(APIView):
    def get(self,request,video_id=None):
        try:
            video=EntertainmentVideos.objects.get(id=video_id)
        except:
            raise NotFound('video not found')
        comment=EntertainmentComment.objects.filter(video=video)
        serializers=EntertainmentCommentSerializer(comment,many=True)
        return Response(serializers.data)
    
    def post(self,request,video_id):
        try:
            video=EntertainmentVideos.objects.get(id=video_id)
        except:
            raise NotFound('video not found')
        
        serializers=EntertainmentCommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(video=video)
            return Response({'msg':'post successful'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors,status=status.HTTP_201_CREATED)
    

