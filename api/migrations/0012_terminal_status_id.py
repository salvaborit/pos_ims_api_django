# Generated by Django 4.1.5 on 2023-01-25 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_status_delete_chip_remove_terminal_acquirer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminal',
            name='status_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.status'),
        ),
    ]
