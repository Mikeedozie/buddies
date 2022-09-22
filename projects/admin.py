from django.contrib import admin
from .models import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'speciality', 'slug', 'gender']
    prepopulated_fields = {'slug': ['first_name','last_name']}
    list_editable = ('speciality',)

admin.site.register(Member,MemberAdmin)