# Generated by Django 3.0.3 on 2020-04-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0008_auto_20200412_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='doc',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='file',
            name='serial',
            field=models.CharField(default='161501D6FE2C4A09B827', max_length=20),
        ),
    ]
