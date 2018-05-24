from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    text = models.TextField(max_length=500)
    status = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

