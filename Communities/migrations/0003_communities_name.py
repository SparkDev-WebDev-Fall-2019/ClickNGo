# Generated by Django 2.2.5 on 2019-11-01 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Communities', '0002_communities_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='communities',
            name='Name',
            field=models.CharField(default='None', max_length=32),
        ),
    ]