from django.db import models

# Create your models here.
class Doctor(models.Model):
  name = models.CharField(max_length = 200)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d')
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20,blank='00000000')
  email = models.EmailField(max_length=50,unique=True,blank=False)
  is_mvp = models.BooleanField(default=True)
  hire_date = models.DateTimeField(auto_now_add =True)
  def __str__(self): # Doctor display >> 影響display table 既Object既'文字表達方式' >> 咩意思 >> 影響display出<Patient: Patient object (1)>
    return self.name