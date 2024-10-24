from datetime import timezone,datetime

from django.contrib.auth.models import User
from django.db import models
from mptt.models import TreeForeignKey, MPTTModel


class Category(MPTTModel):
    name = models.CharField(max_length=200, verbose_name='Название')
    slag = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name = "children",
        on_delete = models.SET_NULL,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name
    
    def was_publisched_recently(self):
        return self.publisched >=(timezone.now() - datetime.timedelta(deys=7))
    
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        

    class MPTTMeta:
        order_insertion_by = ['name']

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slag = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=9)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey (
        Category, 
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField (Tag, related_name="post")
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def NAME(self):
        return u"%s..."% (self.title[:8])
        
    def was_publisched_recently(self):
        return self.publisched >=(timezone.now() - datetime.timedelta(deys=7))   
    
    def __str__(self):
        return self.title
    
    

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    serves = models.CharField(max_length=100)
    pre_time = models.PositiveIntegerField(default=0)
    cooc_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    directions =models.TextField()
    post = models.ForeignKey(
        Post, 
        related_name='recipe', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    
    def POST(self):
        return u"%s..."% (self.post.title[:8])
    
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)