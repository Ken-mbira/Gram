# Generated by Django 3.2.8 on 2021-10-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_path',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
