# Generated by Django 4.1.5 on 2023-02-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0012_alter_placeimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='places/'),
        ),
    ]