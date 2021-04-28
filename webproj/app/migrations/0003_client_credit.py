# Generated by Django 3.1.7 on 2021-04-27 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_client_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='credit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
