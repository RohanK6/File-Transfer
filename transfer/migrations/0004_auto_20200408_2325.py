# Generated by Django 3.0.3 on 2020-04-09 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0003_auto_20200408_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='serial',
            field=models.CharField(default='F8994E29AE1E46CABC05', max_length=6, unique=True),
        ),
    ]
