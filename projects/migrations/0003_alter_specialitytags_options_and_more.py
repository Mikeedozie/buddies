# Generated by Django 4.1.1 on 2022-09-22 02:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_member_active_member_date_joined_specialitytags_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specialitytags',
            options={'verbose_name_plural': 'Speciality Tags'},
        ),
        migrations.AddField(
            model_name='specialitytags',
            name='speciality',
            field=models.ManyToManyField(related_name='speciality_area', to='projects.member'),
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='projects.member'),
        ),
        migrations.RemoveField(
            model_name='specialitytags',
            name='member',
        ),
        migrations.AddField(
            model_name='specialitytags',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='member_speciality', to='projects.member'),
            preserve_default=False,
        ),
    ]