# Generated by Django 5.1.1 on 2024-12-11 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0005_class'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['nazov'], 'verbose_name': 'Trieda', 'verbose_name_plural': 'Triedy'},
        ),
    ]
