# Generated by Django 4.1.1 on 2022-10-05 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_member_image_delete_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialitytags',
            name='speciality',
            field=models.CharField(choices=[('Git/Github', 'Git/Github'), ('Shell', 'Shell'), ('Emacs', 'Emacs'), ('VI', 'Vi'), ('C', 'C'), ('Python', 'Python'), ('Javascript', 'Javascript'), ('Flask', 'Flask'), ('MySQL', 'MySQL'), ('Node Js', 'Node Js')], max_length=100),
        ),
    ]