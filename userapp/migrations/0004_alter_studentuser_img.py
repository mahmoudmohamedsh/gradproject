# Generated by Django 3.2.12 on 2022-04-24 23:54

from django.db import migrations, models
import userapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_studentuser_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='img',
            field=models.ImageField(blank=True, default='', null=True, upload_to=userapp.models.uploat_to),
        ),
    ]