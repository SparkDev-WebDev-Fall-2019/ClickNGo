# Generated by Django 2.2.5 on 2019-11-05 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20191018_2342'),
        ('Communities', '0006_remove_communities_admin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Communities',
            new_name='Community',
        ),
    ]
