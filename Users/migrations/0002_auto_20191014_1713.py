# Generated by Django 2.1.7 on 2019-10-14 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AddField(
            model_name='profile',
            name='profilePic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]