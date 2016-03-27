# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_auto_20160327_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='approve',
            new_name='approved',
        ),
    ]
