from pyexpat import model
from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True)
    like = models.IntegerField()
    dislike = models.IntegerField()
 
    def __str__(self):
        return self.title
 

class PostImage(models.Model):
    post = models.ForeignKey(Posts, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
    def __str__(self):
        return self.post.title