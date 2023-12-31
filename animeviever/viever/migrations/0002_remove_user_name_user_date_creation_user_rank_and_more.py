# Generated by Django 4.1.7 on 2023-07-29 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viever', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='date_creation',
            field=models.DateField(default=datetime.date(2023, 7, 29)),
        ),
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('Новичек', 'Новичек'), ('ученик', 'ученик')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anime',
            name='date_time',
            field=models.DateField(default=datetime.date(2023, 7, 29)),
        ),
    ]
