# Generated by Django 2.2.5 on 2019-11-01 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20191018_2342'),
        ('Communities', '0003_communities_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communities',
            name='User',
        ),
        migrations.AddField(
            model_name='communities',
            name='User',
            field=models.ManyToManyField(to='Users.Profile'),
        ),
    ]
