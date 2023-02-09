from django.contrib import admin
from .models import Youtube

# Register your models here
#
class YoutubeAdmin(admin.ModelAdmin):
    model = Youtube

    list_display = (
        'Vedio_id','id', 'link', 'title')
    fieldsets = (
        ('Youtube', {'fields': (
            'Vedio_id', 'id', 'link', 'title'
        )}),
    )

admin.site.register(Youtube, YoutubeAdmin)
