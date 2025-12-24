from django.db import models

# Create your models here.
class Patient(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  phone = models.CharField(max_length=20)
  gender = models.CharField(max_length=10, default='Unknown')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name