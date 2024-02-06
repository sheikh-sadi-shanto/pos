from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# Create your models here.


def validate_video_size(value):
    max_size=300*1024*1024
    file_size=value.size
    if max_size<file_size:
        raise ValueError('this file is more than 300MB ')
    return value


class CrimeVideos(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    video=models.FileField(upload_to='videos',validators=[FileExtensionValidator(allowed_extensions=['MOV','mp4','mkv','webm']),validate_video_size])
    description=models.TextField()
    title=models.CharField(max_length=300)
    is_solved=models.BooleanField(default=False)
    is_onboard=models.BooleanField(default=False)
    