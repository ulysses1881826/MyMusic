# Generated by Django 2.2.3 on 2019-07-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20190718_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.CharField(max_length=30, verbose_name='user'),
        ),
    ]