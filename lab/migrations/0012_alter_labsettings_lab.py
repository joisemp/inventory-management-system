# Generated by Django 4.2 on 2024-08-05 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0011_alter_systemcomponent_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labsettings',
            name='lab',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='lab.lab'),
        ),
    ]
