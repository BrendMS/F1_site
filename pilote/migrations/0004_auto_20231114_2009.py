# Generated by Django 2.2.28 on 2023-11-14 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pilote', '0003_auto_20231113_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='photo',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipement',
            name='photo',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]