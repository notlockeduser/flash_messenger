# Generated by Django 2.2.12 on 2020-12-13 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_userinfo_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='friends',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
