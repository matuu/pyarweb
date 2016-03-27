# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20160326_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='is_active',
        ),
        migrations.AddField(
            model_name='job',
            name='ts_moderate',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='user_moderate',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
