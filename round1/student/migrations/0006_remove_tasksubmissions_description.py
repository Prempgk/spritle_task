# Generated by Django 4.1.7 on 2023-03-09 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_tasksubmissions_masterdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasksubmissions',
            name='Description',
        ),
    ]
