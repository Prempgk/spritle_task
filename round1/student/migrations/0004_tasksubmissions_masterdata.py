# Generated by Django 4.1.7 on 2023-03-08 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_remove_master_mobileno'),
        ('student', '0003_tasksubmissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksubmissions',
            name='MasterData',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='master.master'),
        ),
    ]