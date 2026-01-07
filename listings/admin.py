from django.contrib import admin
from .models import Listing,Subject
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from taggit.forms import TagWidget
from django.db import models
from django.forms import NumberInput
# Register your models here.
class ListingAdminForm(forms.ModelForm):
  # model data field
  profession = forms.ModelMultipleChoiceField(
    queryset = Subject.objects.all(),
    required=False,
    label="Select Professionals",
    # display, this time use 大階display
    widget = FilteredSelectMultiple(verbose_name="Professionals",
                                    is_stacked=False , 
                                    attrs={'rows':'5'}
    )
  )

  class Meta:
    model=Listing
    fields='__all__'
    widgets = {"services":TagWidget()}
  
# modify to dropdown function
# '__' -> double underscore -> private variable -> share def XX: (function)
# __xyz__ -> Dunder
# IntegerField() default 20 digits
class ListingAdmin(admin.ModelAdmin):
  form = ListingAdminForm
  # admin page show 咩column
  list_display = 'id','title','district','is_published','rooms','doctor','tag_list','display_professions'
  # admin page 用咩做filter
  list_filter=('doctor','services')
  list_display_links='id','title'
  list_editable = 'is_published','rooms'
  search_fields = 'title','district','doctor__name','services__name','profession__name'
  list_per_page=25
  formfield_overrides = {
    models.IntegerField:{
      "widget":NumberInput(attrs={"size":"5"})
    }
  }
  show_facets = admin.ShowFacets.ALWAYS
  def get_queryset(self,request):
    return super().get_queryset(request).prefetch_related("services","profession")

  def display_professions(self,obj):
    return ", ".join([subject.name for subject in obj.profession.all()]) or "None"
  display_professions.short_description = "Professions"

class SubjectAdmin(admin.ModelAdmin):
  list_display = "name",
  search_fields = "name",

admin.site.register(Listing,ListingAdmin)
admin.site.register(Subject,SubjectAdmin)