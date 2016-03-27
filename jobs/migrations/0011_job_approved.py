# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20151127_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='approved',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
