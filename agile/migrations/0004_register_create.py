# Generated by Django 2.2.1 on 2020-07-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0003_auto_20200707_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
