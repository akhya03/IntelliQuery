from django.db import models

# Create your models here.
class SearchResult(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
