# Generated by Django 5.0 on 2024-02-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_datauser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datauser',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
