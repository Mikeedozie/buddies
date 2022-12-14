# Generated by Django 4.1.1 on 2022-09-22 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('speciality', models.CharField(choices=[('GIT/GITHUB', 'Git/Github'), ('SHELL', 'Shell'), ('EMACS', 'Emacs'), ('VI', 'Vi'), ('C', 'C'), ('PYTHON', 'Python')], max_length=10)),
                
            ],
        ),
    ]
