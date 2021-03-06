# Generated by Django 2.0.12 on 2019-09-11 17:37

import django_md_editor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("cooggerapp", "0007_ghost_user")]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="body",
            field=django_md_editor.models.EditorMdField(
                default="",
                help_text="Your content | problem | question | or anything else",
                verbose_name="",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="content",
            name="title",
            field=models.CharField(
                default="", help_text="Be sure to choose the best title", max_length=200
            ),
            preserve_default=False,
        ),
    ]
