# Generated by Django 4.1.5 on 2023-02-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_options_alter_student_dateofbirth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Student_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]