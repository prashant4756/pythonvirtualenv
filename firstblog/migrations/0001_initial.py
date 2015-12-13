# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('bookName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('libraryName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='library',
            field=models.ForeignKey(to='firstblog.Library'),
        ),
    ]
