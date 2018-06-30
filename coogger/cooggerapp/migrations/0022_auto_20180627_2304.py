# Generated by Django 2.0 on 2018-06-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooggerapp', '0021_auto_20180626_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(blank=True, choices=[('tutorial', 'tutorial'), ('idea', 'idea'), ('design-graphic', 'design-graphic'), ('development', 'development'), ('question-answer', 'question-answer'), ('translation', 'translation'), ('discussion', 'discussion')], help_text='select content category', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='status',
            field=models.CharField(choices=[('rejected', 'rejected'), ('approved', 'approved')], max_length=30, verbose_name="content's status"),
        ),
    ]