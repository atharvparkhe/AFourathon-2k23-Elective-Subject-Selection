# Generated by Django 4.2.2 on 2023-06-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_studentmodel_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='teacher'),
        ),
    ]