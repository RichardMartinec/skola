# Generated by Django 5.1.1 on 2024-12-11 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0002_ucitel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ucitel',
            new_name='Teacher',
        ),
    ]
