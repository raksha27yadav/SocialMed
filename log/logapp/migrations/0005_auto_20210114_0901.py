# Generated by Django 3.1.5 on 2021-01-14 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logapp', '0004_auto_20210113_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmsg',
            name='image',
            field=models.ImageField(default='', upload_to='logapp/images'),
        ),
    ]