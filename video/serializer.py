from rest_framework import serializers
from video.models import CrimeVideos


class CrimeVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeVideos
        fields = ['id','description','title','is_solved','is_onboard']  # Adjust fields according to your model
