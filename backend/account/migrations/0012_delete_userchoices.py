# Generated by Django 5.0 on 2024-02-25 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_user_courses'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserChoices',
        ),
    ]
