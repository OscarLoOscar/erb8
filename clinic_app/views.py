from django.shortcuts import render

# Create your views here.
from clinic_app.models import Patient

# method 1 : direct create and save
# Patient.objects.create(name="Oscar",age = 25,phone='123345678')

# method 2 : create class first , setattr , then save
class Patient:
  def __init__(self,name,age,gender,phone):
    self.name = name
    self.age = age
    self.gender = gender
    self.phone = phone

new_patient_1 = Patient()
setattr('Alice',30,'Female','87654321')
new_patient_1.save()