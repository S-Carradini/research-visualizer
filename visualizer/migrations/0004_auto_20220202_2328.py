# Generated by Django 2.2.26 on 2022-02-02 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0003_auto_20220202_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scopusclassification',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]