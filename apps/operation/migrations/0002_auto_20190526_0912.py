# Generated by Django 2.2 on 2019-05-26 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfavorite',
            old_name='name',
            new_name='user',
        ),
    ]
