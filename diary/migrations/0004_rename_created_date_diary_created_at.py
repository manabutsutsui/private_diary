# Generated by Django 5.0.2 on 2024-02-25 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_rename_created_at_diary_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='created_date',
            new_name='created_at',
        ),
    ]
