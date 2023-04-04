# Generated by Django 4.1.7 on 2023-03-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content_teacher',
            name='position_title',
            field=models.CharField(default='头衔', max_length=100, verbose_name='职位、职称'),
        ),
        migrations.AlterField(
            model_name='friendly_link',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='链接名称'),
        ),
    ]
