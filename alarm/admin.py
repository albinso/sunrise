from django.contrib import admin
from . import models
# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Artist, ArtistAdmin)
