# Generated by Django 4.1.5 on 2023-02-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Students_data', 'verbose_name_plural': 'Students_data'},
        ),
        migrations.AlterField(
            model_name='student',
            name='DateofBirth',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
