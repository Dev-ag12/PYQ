# Generated by Django 5.0 on 2024-02-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=models.CharField(choices=[('Tutorials', 'Tutorials'), ('Minor', 'Minor'), ('Quiz', 'Quiz')], max_length=50),
        ),
    ]
