from django.db import models
from doctors.models import Doctor
from .choices import district_groups_choices,room_type_choices,bedroom_choices
from taggit.managers import TaggableManager

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
          return self.name

class Listing(models.Model):
  doctor = models.ForeignKey(Doctor,on_delete= models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  district = models.CharField(max_length=50,choices=district_groups_choices)# 輔助性，唔洗'make makemigrations'
  description = models.TextField(blank=True)
  # services = models.TextField(blank=True)
  services = TaggableManager(verbose_name="Services")
  service = models.IntegerField()
  room_type = models.CharField(max_length=200,default='',choices=room_type_choices.items())
  rooms = models.CharField(max_length=2,choices=bedroom_choices.items())
  # profession = models.CharField(max_length=200,default='')
  profession = models.ManyToManyField(Subject,blank=True)
  photo_main = models.ImageField(upload_to = 'photos/%Y/%d',blank=True)
  photo_1 = models.ImageField(upload_to = 'photos/%Y/%d',blank=True)
  photo_2 = models.ImageField(upload_to = 'photos/%Y/%d',blank=True)
  photo_3 = models.ImageField(upload_to = 'photos/%Y/%d',blank=True)
  photo_4 = models.ImageField(upload_to = 'photos/%Y/%d',blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.title
  
  def tag_list(self):
    return u", ".join(tag.name for tag in self.services.all())
  
  class Meta:
    ordering = ['-list_date']
    indexes = [models.Index(fields = ['list_date'])]

    def __str__(self):
        return self.title