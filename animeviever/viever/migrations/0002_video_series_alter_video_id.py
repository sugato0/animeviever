# Generated by Django 4.1.7 on 2023-07-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viever', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='series',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]