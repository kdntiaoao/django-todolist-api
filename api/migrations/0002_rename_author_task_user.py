# Generated by Django 4.1.5 on 2023-01-13 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='author',
            new_name='user',
        ),
    ]
