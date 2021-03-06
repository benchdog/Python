# Generated by Django 3.1.1 on 2020-12-29 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_viid_system',
            name='count',
            field=models.SmallIntegerField(null=True, verbose_name=11),
        ),
        migrations.AlterField(
            model_name='t_viid_system',
            name='ipv6Addr',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='t_viid_system',
            name='receiveAddr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='t_viid_system',
            name='subscribeDetail',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
