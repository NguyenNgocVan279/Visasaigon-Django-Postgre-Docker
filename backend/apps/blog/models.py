from django.db import models
from django.utils.text import slugify
from apps.core_app.models import TimeStampedModel

class BlogCategory(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name


class BlogTag(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name


class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(BlogCategory,on_delete=models.SET_NULL,null=True,related_name="posts")
    tags = models.ManyToManyField(BlogTag,blank=True,related_name="posts")
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
