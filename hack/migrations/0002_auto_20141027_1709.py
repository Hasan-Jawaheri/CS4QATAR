# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='aliaa',
        ),
        migrations.AddField(
            model_name='user',
            name='CH1_stage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.CharField(max_length=128, default=0),
            preserve_default=False,
        ),
    ]
