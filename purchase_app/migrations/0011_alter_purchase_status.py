# Generated by Django 4.1.5 on 2023-04-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_app', '0010_rename_done_by_purchase_purchased_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed')], max_length=10),
        ),
    ]
