# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0002_auto_20141027_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='CH1_Hash_value',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
