# Generated by Django 3.0.3 on 2020-04-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0011_auto_20200412_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='file',
            name='serial',
            field=models.CharField(default='61FCD750EE1441DBA587', max_length=20),
        ),
    ]
