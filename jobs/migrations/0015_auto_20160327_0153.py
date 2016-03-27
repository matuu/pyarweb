# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_auto_20160326_2359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='approved',
            new_name='approve',
        ),
    ]
