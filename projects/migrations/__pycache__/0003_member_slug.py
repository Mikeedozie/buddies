# Generated by Django 4.1.1 on 2022-09-22 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_members_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
