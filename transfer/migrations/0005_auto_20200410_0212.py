# Generated by Django 3.0.3 on 2020-04-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0004_auto_20200408_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='serial',
            field=models.CharField(default='26B6A6E7C49341B89769', max_length=6),
        ),
    ]
