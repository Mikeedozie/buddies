# Generated by Django 4.1.1 on 2022-09-23 14:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SpecialityTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ManyToManyField(to='projects.member')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile-images')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.member')),
            ],
        ),
    ]
