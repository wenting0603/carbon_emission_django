# Generated by Django 3.2.7 on 2022-10-14 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0002_testdb_carbon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdb',
            name='carbon',
            field=models.CharField(default='1', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='testdb',
            name='distance',
            field=models.CharField(max_length=1000000),
        ),
    ]
