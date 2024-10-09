from django.db import models

# Create your models here.


class BlogCategory(models.Model):
    id = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=255)
    categoryDescription = models.TextField(null=True)
    image = models.ImageField(upload_to='blogCategory',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)





class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    status = models.CharField(default='Pending',max_length=255)
    blogCategory = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='blog',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)


class Communities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='communities',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)