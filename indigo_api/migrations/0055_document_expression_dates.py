# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-30 19:37
from __future__ import unicode_literals
import datetime

from django.db import migrations


def ensure_expression_dates(apps, schema_editor):
    Work = apps.get_model("indigo_api", "Work")
    Document = apps.get_model("indigo_api", "Document")
    db_alias = schema_editor.connection.alias

    default_date = datetime.date(1980, 1, 1)

    for document in Document.objects.filter(expression_date=None).using(db_alias).all():
        document.expression_date = document.work.publication_date or datetime
        document.save()


class Migration(migrations.Migration):

    dependencies = [
        ('indigo_api', '0054_view_published_doc_perms'),
    ]

    operations = [
        migrations.RunPython(ensure_expression_dates, migrations.RunPython.noop),
    ]
