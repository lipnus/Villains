# Generated by Django 2.1.dev20171005184450 on 2018-01-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('villains', '0005_auto_20180113_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='villain',
            name='agree',
            field=models.IntegerField(default=0),
        ),
    ]
