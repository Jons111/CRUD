from django.contrib import admin
from myfiles.models import Teacher,Fan
# Register your models here.
class AdminTech(admin.ModelAdmin):
    list_display = ['ism','fam','yosh','fan','sana']

admin.site.register(Teacher,AdminTech)


class AdminFan(admin.ModelAdmin):
    list_display = ['nomi']

admin.site.register(Fan,AdminFan)