# Generated by Django 3.2.8 on 2021-10-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_image_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]