# Generated by Django 4.2.2 on 2023-06-14 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.baseuser',),
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('time_table', models.ImageField(blank=True, null=True, upload_to='time-table')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='upload')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('post', models.CharField(max_length=50)),
                ('experience', models.FloatField(default=1.0)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='teacher')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_teacher', to='authentication.departmentmodel')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.baseuser',),
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('roll_no', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='student')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_department', to='authentication.departmentmodel')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.baseuser',),
        ),
    ]
