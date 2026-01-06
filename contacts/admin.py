from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  list_display = ('id','listing','name','email','phone','contact_date')
  list_display_links = ('id','name')
  search_fields = ('listing','name','email','phone')
  list_per_page = 25

admin.site.register(Contact,ContactAdmin)