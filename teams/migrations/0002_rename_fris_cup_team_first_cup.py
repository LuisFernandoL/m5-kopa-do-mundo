# Generated by Django 4.2.5 on 2023-09-28 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='fris_cup',
            new_name='first_cup',
        ),
    ]
