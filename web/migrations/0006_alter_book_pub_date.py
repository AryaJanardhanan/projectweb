# Generated by Django 5.1.5 on 2025-02-07 05:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_book_fl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
