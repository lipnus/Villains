# Generated by Django 2.1.dev20171005184450 on 2018-01-24 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('villains', '0009_auto_20180124_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agreer',
            old_name='villain_id',
            new_name='villain',
        ),
    ]
