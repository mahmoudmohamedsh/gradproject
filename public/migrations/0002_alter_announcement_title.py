# Generated by Django 3.2.12 on 2022-04-25 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]