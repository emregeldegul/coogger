# Generated by Django 2.0.12 on 2019-09-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("cooggerapp", "0004_auto_20190831_1243")]

    operations = [
        migrations.RenameField(
            model_name="userprofile", old_name="description", new_name="bio"
        ),
        migrations.RenameField(
            model_name="topic", old_name="definition", new_name="description"
        ),
        migrations.RenameField(
            model_name="utopic", old_name="definition", new_name="description"
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="title",
            field=models.CharField(
                choices=[
                    ("author", "author"),
                    ("contributor", "contributor"),
                    ("core-developer", "core developer"),
                    ("founder", "founder"),
                    ("moderator", "moderator"),
                    ("sponsor", "sponsor"),
                    ("user", "user"),
                ],
                default="user",
                help_text="Title",
                max_length=30,
                verbose_name="title",
            ),
        ),
    ]
