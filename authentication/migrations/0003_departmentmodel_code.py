# Generated by Django 4.2.2 on 2023-06-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_teachermodel_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentmodel',
            name='code',
            field=models.CharField(default='MECH', max_length=5),
        ),
    ]
