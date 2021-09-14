from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
    class Category(models.TextChoices):
        General = 'general'
        Notice = 'notice'
        info = 'info'

    category = models.CharField(
        max_length=100,
        choices=Category.choices,
        default=Category.General
    ) 

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[{}] {}'.format(self.user.username, self.title)

    class Meta:
        db_table = 'post_table'
        verbose_name = 'post'
        verbose_name_plural = 'posts'