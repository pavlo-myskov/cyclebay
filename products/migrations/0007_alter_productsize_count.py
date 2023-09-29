# Generated by Django 3.2.21 on 2023-09-29 16:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productsize_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='count',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)]),
        ),
    ]
