# Generated by Django 3.1.5 on 2021-01-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0008_profilecover_nme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmsg',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='logapp/images'),
        ),
        migrations.AlterField(
            model_name='profilecover',
            name='coverphoto',
            field=models.ImageField(blank=True, default='', upload_to='logapp/images'),
        ),
        migrations.AlterField(
            model_name='profilecover',
            name='profile',
            field=models.ImageField(blank=True, default='', upload_to='logapp/images'),
        ),
    ]
