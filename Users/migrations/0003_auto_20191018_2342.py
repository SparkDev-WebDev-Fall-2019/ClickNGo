# Generated by Django 2.2.5 on 2019-10-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20191014_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilePic',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
