from django.db import models

# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    pcode = models.CharField(max_length=10, unique=True)
    pname = models.CharField(max_length=20)
    unitprice = models.IntegerField(default=0)
    discountrate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imgfile = models.ImageField(null=True, blank=True)

# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)

    contents = models.TextField()

    def __str__(self):
        return self.postname



