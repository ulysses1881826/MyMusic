# Generated by Django 2.2.3 on 2019-07-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='label_name',
            field=models.CharField(max_length=20, verbose_name='class label'),
        ),
    ]
