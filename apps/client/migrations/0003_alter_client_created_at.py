# Generated by Django 4.2.11 on 2024-05-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
