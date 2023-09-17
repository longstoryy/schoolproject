from django.contrib import admin
from .models import Member,Entry,Pupil

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date","phone","photo","text","date_added")
  
admin.site.register(Member, MemberAdmin)
admin.site.register(Entry)

admin.site.register(Pupil)

