# Generated by Django 4.1.1 on 2022-10-15 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_topicoverview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicoverview',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='overview', to='projects.topic'),
        ),
    ]
