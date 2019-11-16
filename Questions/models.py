from django.db import models
from django.contrib.auth.models import User
from Users.models import Profile
from django.urls import reverse

# Create your models here.
class Question(models.Model):
    User = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Question = models.CharField(max_length=256)
    Description = models.CharField(max_length=10000)
    class Meta:
      verbose_name_plural = "Questions"

    def __str__(self):
        return str(self.Question)
    
    def get_absolute_url(self):
        return reverse('Question:questionDetail', args=[self.Question])

class Response(models.Model):
    User = models.ForeignKey(Profile, on_delete=(models.CASCADE))
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Response = models.CharField(max_length = 10000)
