# Generated by Django 4.0 on 2022-01-03 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_produto_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='teste',
        ),
    ]
