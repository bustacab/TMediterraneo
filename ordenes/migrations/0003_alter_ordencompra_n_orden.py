# Generated by Django 4.1.2 on 2022-10-26 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0002_alter_ordencompra_n_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordencompra',
            name='n_orden',
            field=models.PositiveIntegerField(),
        ),
    ]
