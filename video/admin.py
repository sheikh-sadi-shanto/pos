from django.contrib import admin
from video.models import *
# Register your models here.

class CrimeVideosAdmin(admin.ModelAdmin):
    list_display=['user','title','view_count','is_onboard','is_solved']
    list_filter=['is_onboard','is_solved']
admin.site.register(CrimeVideos,CrimeVideosAdmin)
admin.site.register(Comment)


class EntertainmentAdmin(admin.ModelAdmin):
    list_display=['user','title','view_count','is_onboard','is_solved']
    list_filter=['is_onboard','is_solved']
admin.site.register(EntertainmentVideos,EntertainmentAdmin)
admin.site.register(EntertainmentComment)