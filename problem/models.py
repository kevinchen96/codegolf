from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Problem(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 300)
    test_in = models.CharField(max_length = 100)
    test_out = models.CharField(max_length = 100)
    par = models.IntegerField(default = 30)

class Score(models.Model):
    problem = models.ForeignKey(Problem)
    user = models.ForeignKey(User)
    score = models.IntegerField()
