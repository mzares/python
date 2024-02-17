from django.db import models
class Headline(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    date = models.DateTimeField(null=True)
    desc= models.CharField(max_length=200, null=True)
    url = models.URLField(null=True, blank=True)
    
    # title = models.CharField(max_length=1000)
    # link = models.URLField()
    # desc= models.CharField(max_length=3000)
    # date = models.DateTimeField()
    # image_src = models.URLField()
    # # enclosure = models.URLField(null=True, blank=True)

def __str__(self):
        return self.title
# Create your models here.
