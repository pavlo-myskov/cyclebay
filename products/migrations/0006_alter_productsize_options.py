# Generated by Django 3.2.21 on 2023-09-24 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_size_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsize',
            options={'ordering': ['size']},
        ),
    ]