# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-15 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=2048, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonPageRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField()),
                ('lastScanData', models.DateTimeField(auto_now_add=True)),
                ('FindData', models.DateTimeField(auto_now_add=True)),
                ('idPage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAPI.Pages')),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('ip', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2048, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('ip', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='personpagerank',
            name='idPerson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAPI.Persons'),
        ),
        migrations.AddField(
            model_name='pages',
            name='sites',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAPI.Sites'),
        ),
        migrations.AddField(
            model_name='keywords',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAPI.Persons'),
        ),
    ]
