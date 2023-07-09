# Generated by Django 4.1.5 on 2023-03-07 11:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_party', '0003_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
