# Generated by Django 4.1.7 on 2023-03-19 04:37

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_alter_database_code_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='database_announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='会议', max_length=30, verbose_name='展示标题')),
                ('time', models.CharField(default='', max_length=20, verbose_name='发布时间')),
                ('announcement_content', tinymce.models.HTMLField(default='', verbose_name='公告内容')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
    ]
