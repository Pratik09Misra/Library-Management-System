# Generated by Django 5.0.6 on 2024-06-03 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_author_name_alter_book_book_add_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_add_date',
            field=models.DateField(default=datetime.date(2024, 6, 4)),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_add_time',
            field=models.TimeField(default=datetime.datetime(2024, 6, 3, 21, 31, 1, 105181, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='issueditem',
            name='issue_date',
            field=models.DateField(default=datetime.date(2024, 6, 4)),
        ),
    ]
