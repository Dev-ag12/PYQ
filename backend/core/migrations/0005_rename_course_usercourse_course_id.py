# Generated by Django 5.0 on 2024-02-25 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_usercourse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercourse',
            old_name='course',
            new_name='course_id',
        ),
    ]