# Generated by Django 4.1.1 on 2022-09-24 00:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_specialitytags_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile-images'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProfileImage',
        ),
    ]
