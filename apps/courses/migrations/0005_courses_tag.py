# Generated by Django 2.2 on 2019-05-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190526_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='课程标签'),
        ),
    ]