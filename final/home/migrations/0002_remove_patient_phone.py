# Generated by Django 2.1.4 on 2019-03-08 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='phone',
        ),
    ]
