# Generated by Django 4.0 on 2022-05-27 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Tasks',
        ),
    ]