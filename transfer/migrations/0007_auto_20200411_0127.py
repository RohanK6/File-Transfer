# Generated by Django 3.0.3 on 2020-04-11 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0006_auto_20200411_0126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='emptyserial',
            new_name='code',
        ),
        migrations.AlterField(
            model_name='file',
            name='serial',
            field=models.CharField(default='C776FBBAA3B046E9B6E6', max_length=20),
        ),
    ]