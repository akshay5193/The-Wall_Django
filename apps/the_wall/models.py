from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User
# Create your models here.


class Post(models.Model):
    post_content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="posts")


class Comment(models.Model):
    comment_content = models.TextField(1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="comments")
    post = models.ForeignKey(Post, related_name="comments")
