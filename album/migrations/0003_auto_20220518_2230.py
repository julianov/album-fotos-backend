# Generated by Django 2.2.12 on 2022-05-18 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20220518_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
