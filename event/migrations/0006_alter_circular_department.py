# Generated by Django 3.2.8 on 2021-10-06 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_circular_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circular',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.department'),
        ),
    ]