# Generated by Django 4.1.5 on 2023-01-11 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0002_sales_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesitem',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
