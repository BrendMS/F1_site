# Generated by Django 2.2.28 on 2023-11-13 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='type',
        ),
    ]