# Generated by Django 4.2.7 on 2024-02-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_student_sname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='strollno',
            field=models.CharField(max_length=100),
        ),
    ]
