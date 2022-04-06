# Generated by Django 4.0.3 on 2022-04-06 17:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FamiliaApp', '0002_remove_familiar_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
