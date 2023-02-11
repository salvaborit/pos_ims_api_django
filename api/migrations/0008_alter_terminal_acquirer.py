# Generated by Django 4.1.5 on 2023-01-24 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_client_acquirer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal',
            name='acquirer',
            field=models.ForeignKey(blank=True, default=5, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='acquirer_name', to='api.acquirer'),
        ),
    ]
