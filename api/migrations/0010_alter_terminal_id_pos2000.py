# Generated by Django 4.1.5 on 2023-01-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_terminal_id_pos2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal',
            name='id_pos2000',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
