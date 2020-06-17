# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin


class Agile(models.Model):
    title = models.TextField(blank=True, null=False, primary_key=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'agile'
        db_table = 'agile_story'


class AgileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')



