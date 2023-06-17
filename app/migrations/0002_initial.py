# Generated by Django 4.2.2 on 2023-06-17 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectmodel',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_subject', to='authentication.departmentmodel'),
        ),
        migrations.AddField(
            model_name='subjectmodel',
            name='teacher',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_teacher', to='authentication.teachermodel'),
        ),
        migrations.AddField(
            model_name='enollmentmodel',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_students', to='authentication.studentmodel'),
        ),
        migrations.AddField(
            model_name='enollmentmodel',
            name='subject_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_subject_1', to='app.subjectmodel'),
        ),
        migrations.AddField(
            model_name='enollmentmodel',
            name='subject_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_subject_2', to='app.subjectmodel'),
        ),
        migrations.AddField(
            model_name='enollmentmodel',
            name='subject_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_subject_3', to='app.subjectmodel'),
        ),
        migrations.AddField(
            model_name='changeelectivemodel',
            name='from_sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_subject', to='app.subjectmodel'),
        ),
        migrations.AddField(
            model_name='changeelectivemodel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_change_elective', to='authentication.studentmodel'),
        ),
        migrations.AddField(
            model_name='changeelectivemodel',
            name='to_sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_subject', to='app.subjectmodel'),
        ),
    ]
