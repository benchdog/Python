# Generated by Django 3.1.1 on 2020-12-29 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20201229_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_viid_system',
            name='type',
            field=models.SmallIntegerField(verbose_name=1),
        ),
    ]
