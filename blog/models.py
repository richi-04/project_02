from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    publish = models.DateTimeField(null=True)

