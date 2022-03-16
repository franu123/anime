from django.db import models


# Create your models here.
class AnimeDetails(models.Model):
    anime_sname = models.CharField(max_length=200)

    def __str__(self):
        return self.anime_sname
