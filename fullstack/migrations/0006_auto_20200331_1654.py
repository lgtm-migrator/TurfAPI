# Generated by Django 3.0.4 on 2020-03-31 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullstack', '0005_auto_20200331_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time_slot_one',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_slot_three',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_slot_two',
            field=models.CharField(max_length=30),
        ),
    ]