# Generated by Django 3.2.9 on 2021-12-07 03:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('IP', models.GenericIPAddressField()),
                ('ap_name', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['ap_name'],
            },
        ),
        migrations.CreateModel(
            name='guestuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netuser', models.CharField(max_length=40)),
                ('netpass', models.CharField(max_length=40)),
                ('wlanID', models.IntegerField(default=4, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('lifetime', models.IntegerField(default=28800, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2592000)])),
                ('description', models.CharField(max_length=40)),
                ('aps', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apiWLC.ap')),
            ],
            options={
                'ordering': ['netuser'],
            },
        ),
    ]
