# Generated by Django 2.2 on 2019-07-25 08:15

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20190725_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情'),
        ),
    ]
