from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=255, default="")

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name



