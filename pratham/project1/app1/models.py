from django.db import models

# Create your models here
class Evaluation(models.Model):
    fac_name=models.CharField()
    subject=models.CharField()
    score=models.CharField()
    email=models.CharField()
    def __str__(self):
        return self.fac_name