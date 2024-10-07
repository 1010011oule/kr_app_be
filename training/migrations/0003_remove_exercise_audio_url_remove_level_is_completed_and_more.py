# Generated by Django 5.1.1 on 2024-10-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_level_section_exercise_userprogress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='audio_url',
        ),
        migrations.RemoveField(
            model_name='level',
            name='is_completed',
        ),
        migrations.RemoveField(
            model_name='userprogress',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer_choices',
            field=models.TextField(default='A: , B: , C: , D: '),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='correct_answer',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='level',
            name='level_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
