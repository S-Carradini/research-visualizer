# Generated by Django 2.2.27 on 2022-02-11 23:51

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0006_auto_20220204_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('query', models.TextField()),
                ('context', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('finished', models.BooleanField(default=False)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SearchResult_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_abbr', models.CharField(db_index=True, max_length=4)),
                ('scopus_id', models.CharField(max_length=16)),
                ('title', models.TextField()),
                ('first_author', models.CharField(blank=True, max_length=128, null=True)),
                ('publication_name', models.TextField()),
                ('scopus_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='visualizer.ScopusSource')),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='visualizer.Search')),
            ],
        ),
        migrations.CreateModel(
            name='SearchResult_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('category_abbr', models.CharField(max_length=4)),
                ('counts', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='visualizer.Search')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
