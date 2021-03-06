# Generated by Django 3.1.5 on 2021-01-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0002_auto_20210112_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmsg',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='logapp/images'),
        ),
        migrations.AlterField(
            model_name='postmsg',
            name='name',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='postmsg',
            name='text',
            field=models.CharField(blank=True, default='', max_length=30000),
        ),
    ]
