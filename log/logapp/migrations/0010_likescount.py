# Generated by Django 3.1.5 on 2021-03-30 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logapp', '0009_auto_20210125_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likescount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check', models.IntegerField()),
                ('postnm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logapp.postmsg')),
                ('usernm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
