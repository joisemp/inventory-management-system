# Generated by Django 4.2 on 2024-06-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_alter_system_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='status',
            field=models.CharField(choices=[('working', 'Working'), ('not_working', 'Not working'), ('item_missing', 'Item missing')], max_length=255),
        ),
    ]
