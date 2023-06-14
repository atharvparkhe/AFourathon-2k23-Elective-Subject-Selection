# Generated by Django 4.2.2 on 2023-06-14 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enollmentmodel',
            name='subject_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_subject_2', to='app.subjectmodel'),
        ),
        migrations.AlterField(
            model_name='enollmentmodel',
            name='subject_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_subject_3', to='app.subjectmodel'),
        ),
        migrations.AlterField(
            model_name='subjectmodel',
            name='intro',
            field=models.URLField(),
        ),
    ]
