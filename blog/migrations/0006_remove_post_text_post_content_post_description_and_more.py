# Generated by Django 5.1.3 on 2024-12-05 07:32

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_thumbnail_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Context'),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Title'),
        ),
    ]
