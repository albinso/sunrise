from django.contrib import admin
from . import models
# Register your models here.


class PlaylistAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.PlayList, PlaylistAdmin)
