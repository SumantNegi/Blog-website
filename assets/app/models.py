from math import trunc
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from froala_editor.fields import FroalaField
from .helpers import*


# Create your models here.
class post( models.Model):
    title= models.CharField(max_length=250)
    author= models.ForeignKey(User,  on_delete=models.CASCADE)
    desc=models.TextField()
    detail=FroalaField()
    slug =models.SlugField(max_length=1000, null=True,blank=True)
    image=models.ImageField(upload_to='image')
    created_at=models.DateTimeField(auto_now_add=True)
    upload_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(post,self).save(*args,**kwargs)