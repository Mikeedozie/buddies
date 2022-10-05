from django.contrib import admin
from .models import Member, SpecialityTags, Topic, Quiz
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'active', 'slug', 'gender']
    prepopulated_fields = {'slug': ['first_name','last_name']}
    list_editable = ('active',)

admin.site.register(Member,MemberAdmin)
admin.site.register(Topic)
admin.site.register(Quiz)
admin.site.register(SpecialityTags)
