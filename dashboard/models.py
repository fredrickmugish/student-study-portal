from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Youtube(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)


    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "youtube"
        verbose_name_plural = "youtube"


    

