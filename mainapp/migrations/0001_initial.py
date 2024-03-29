# Generated by Django 5.0 on 2024-02-14 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
