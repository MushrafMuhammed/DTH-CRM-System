# Generated by Django 5.0.1 on 2024-02-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_lead_lead_status_alter_lead_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
