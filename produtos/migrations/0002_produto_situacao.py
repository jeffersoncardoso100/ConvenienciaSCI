# Generated by Django 4.2.2 on 2023-07-05 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='situacao',
            field=models.CharField(default=datetime.datetime(2023, 7, 5, 0, 54, 10, 783342, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
    ]
