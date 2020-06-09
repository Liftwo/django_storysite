from django.contrib import admin

# Register your models here.
from .models import Teacher, Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Teacher)
admin.site.register(Photo, PhotoAdmin)
