# Generated by Django 2.2.1 on 2020-06-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
