# Generated by Django 4.1.5 on 2023-02-08 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_app', '0009_rename_myuser_purchase_done_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='done_by',
            new_name='purchased_by',
        ),
    ]
