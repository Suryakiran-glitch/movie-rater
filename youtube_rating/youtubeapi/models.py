from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
 title : models.CharField(max_length = 20)
 description : models.TextField(max_length=256 , blank=True)
 url : models.CharField(max_length = 50)
 category : models.CharField(max_length = 50)
 subcategory : models.CharField(max_length = 50)
 author : models.CharField(max_length = 50)

 def rating_average(self):
   ratings = Rating.objects.filter(video=self)
   sum = 0
   for rating in ratings:
    sum = sum+rating

    if(len(ratings) > 0):
     return sum/len(ratings)

    else :
     return 0 


class Rating(models.Model):
 video = models.ForeignKey(Video , on_delete=models.CASCADE)
 user = models.ForeignKey(User , on_delete=models.CASCADE)
 rating : models.IntegerField()
 comments : models.TextField(max_length=200)

 class Meta:
  unique_together = (('user' , 'video'),)
  index_together = (('user' , 'video'),)