# Generated by Django 4.1.7 on 2023-03-13 13:14

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='文章标题')),
                ('body', tinymce.models.HTMLField(verbose_name='内容')),
            ],
        ),
        migrations.CreateModel(
            name='content_teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_ID', models.CharField(default='', max_length=20, verbose_name='教师ID')),
                ('position_title', models.CharField(default='头衔', max_length=20, verbose_name='职位、职称')),
                ('state', models.CharField(default='', max_length=10, verbose_name='状态')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('teacher', models.CharField(default='', max_length=10, verbose_name='姓名')),
                ('photo_url', models.CharField(default='', max_length=100, verbose_name='图片路径')),
                ('introduction', tinymce.models.HTMLField(default='', verbose_name='介绍内容')),
                ('img', models.ImageField(default='python manage.py makemigrations', upload_to='app01/static/media_for_teacherphoto', verbose_name='教师头像')),
            ],
        ),
        migrations.CreateModel(
            name='content_technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='科研成果', max_length=30, verbose_name='展示标题')),
                ('wenzhang_title', models.CharField(default='科研成果', max_length=30, verbose_name='文章标题')),
                ('technology_content', tinymce.models.HTMLField(default='', verbose_name='科研内容')),
                ('publisher', models.CharField(default='', max_length=10, verbose_name='发布人')),
                ('time', models.CharField(default='', max_length=20, verbose_name='发布时间')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
        migrations.CreateModel(
            name='database_academic_books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='展示标题', max_length=30, verbose_name='展示标题')),
                ('wenzhang_title', models.CharField(default='书籍标题', max_length=30, verbose_name='书籍标题')),
                ('time', models.CharField(default='', max_length=20, verbose_name='发布时间')),
                ('book_content', tinymce.models.HTMLField(default='', verbose_name='书籍内容')),
                ('author', models.CharField(default='', max_length=10, verbose_name='作者')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
        migrations.CreateModel(
            name='database_academic_dissertation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='展示标题', max_length=30, verbose_name='展示标题')),
                ('wenzhang_title', models.CharField(default='论文标题', max_length=30, verbose_name='论文标题')),
                ('time', models.CharField(default='', max_length=20, verbose_name='发布时间')),
                ('dissertation_content', tinymce.models.HTMLField(default='', verbose_name='论文内容')),
                ('publisher', models.CharField(default='', max_length=10, verbose_name='发布人')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
        migrations.CreateModel(
            name='database_academic_lectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='展示标题', max_length=30, verbose_name='展示标题')),
                ('theme', models.CharField(default='讲座主题', max_length=30, verbose_name='讲座主题')),
                ('organizer', models.CharField(default='主办单位', max_length=30, verbose_name='主办单位')),
                ('time', models.CharField(default='', max_length=20, verbose_name='时间')),
                ('speaker', models.CharField(default='', max_length=10, verbose_name='主讲人')),
                ('place', models.CharField(default='', max_length=30, verbose_name='地点')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
            options={
                'verbose_name': '讲座',
                'verbose_name_plural': '讲座',
            },
        ),
        migrations.CreateModel(
            name='database_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(default='', max_length=20, verbose_name='发布时间')),
                ('zhanshi_title', models.CharField(max_length=20, verbose_name='展示标题')),
                ('code_url', models.CharField(default='', max_length=100, verbose_name='代码路径')),
                ('code_title', models.CharField(default='代码标题', max_length=30, verbose_name='代码标题')),
                ('code_introduction', tinymce.models.HTMLField(default='', verbose_name='代码介绍')),
                ('code', models.FileField(default='python manage.py makemigrations', upload_to='app01/static/media_for_code', verbose_name='代码文件')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
        migrations.CreateModel(
            name='database_conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='会议', max_length=30, verbose_name='展示标题')),
                ('wenzhang_title', models.CharField(default='会议标题', max_length=30, verbose_name='会议标题')),
                ('time', models.CharField(default='', max_length=20, verbose_name='发布时间')),
                ('conference_content', tinymce.models.HTMLField(default='', verbose_name='会议内容')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
            options={
                'verbose_name': '会议',
                'verbose_name_plural': '会议',
            },
        ),
        migrations.CreateModel(
            name='database_conference_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='会议报告', max_length=30, verbose_name='展示标题')),
                ('wenzhang_title', models.CharField(default='报告标题', max_length=30, verbose_name='报告标题')),
                ('time', models.CharField(default='', max_length=20, verbose_name='发布时间')),
                ('conference_report_content', tinymce.models.HTMLField(default='', verbose_name='报告内容')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
        migrations.CreateModel(
            name='database_daily_activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='日常活动', max_length=30, verbose_name='展示标题')),
                ('wenzhang_title', models.CharField(default='活动标题', max_length=30, verbose_name='活动标题')),
                ('time', models.CharField(default='', max_length=20, verbose_name='活动时间')),
                ('activity_content', tinymce.models.HTMLField(default='', verbose_name='活动内容')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
        migrations.CreateModel(
            name='database_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='展示标题', max_length=30, verbose_name='展示标题')),
                ('time', models.CharField(default='', max_length=20, verbose_name='时间')),
                ('data_content', tinymce.models.HTMLField(default='', verbose_name='数据内容')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
        migrations.CreateModel(
            name='database_news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='python manage.py makemigrations', upload_to='app01/static/media_for_news', verbose_name='实验室新闻图片')),
                ('zhanshi_title', models.CharField(default='展示标题', max_length=30, verbose_name='展示标题')),
                ('news_title', models.CharField(default='新闻标题', max_length=30, verbose_name='新闻标题')),
                ('time', models.CharField(default='', max_length=20, verbose_name='时间')),
                ('photo_url', models.CharField(default='', max_length=100, verbose_name='图片路径')),
                ('news_introduction', tinymce.models.HTMLField(default='', verbose_name='新闻内容')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
        migrations.CreateModel(
            name='database_online_resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='资源标题', max_length=30, verbose_name='资源展示标题')),
                ('resource_url', models.CharField(default='', max_length=100, verbose_name='资源网址')),
            ],
        ),
        migrations.CreateModel(
            name='database_publicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='python manage.py makemigrations', upload_to='app01/static/media_for_publicity', verbose_name='宣传图片')),
                ('photo_url', models.CharField(default='', max_length=100, verbose_name='图片路径')),
            ],
        ),
        migrations.CreateModel(
            name='Fangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fangan', tinymce.models.HTMLField(default='实验室培养方案', verbose_name='培养方案')),
            ],
        ),
        migrations.CreateModel(
            name='friendly_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='链接名称')),
                ('website', models.CharField(default='', max_length=100, verbose_name='网址')),
            ],
        ),
        migrations.CreateModel(
            name='Newworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField(default='实验室简介', verbose_name='简介内容')),
            ],
        ),
        migrations.CreateModel(
            name='other_achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='其他成果', max_length=30, verbose_name='展示标题')),
                ('wenzhang_title', models.CharField(default='其他成果', max_length=30, verbose_name='文章标题')),
                ('time', models.CharField(default='', max_length=20, verbose_name='发布时间')),
                ('achievement_content', tinymce.models.HTMLField(default='', verbose_name='成果内容')),
                ('publisher', models.CharField(default='', max_length=15, verbose_name='发布人')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
        migrations.CreateModel(
            name='research_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.CharField(default='', max_length=20, verbose_name='学号')),
                ('name', models.CharField(default='', max_length=10, verbose_name='姓名')),
                ('year', models.CharField(default='', max_length=6, verbose_name='出生年份')),
                ('academy', models.CharField(default='', max_length=20, verbose_name='学院')),
                ('zhanshi_titile', models.CharField(max_length=20, verbose_name='展示标题')),
                ('photo_url', models.CharField(default='', max_length=100, verbose_name='图片路径')),
                ('introduction', tinymce.models.HTMLField(default='', verbose_name='介绍内容')),
                ('img', models.ImageField(default='python manage.py makemigrations', upload_to='app01/static/media_for_studentphoto', verbose_name='学生头像')),
            ],
        ),
        migrations.CreateModel(
            name='zhuanye_achievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhanshi_title', models.CharField(default='专业成果', max_length=30, verbose_name='展示标题')),
                ('wenzhang_title', models.CharField(default='专业成果', max_length=30, verbose_name='文章标题')),
                ('time', models.CharField(default='', max_length=20, verbose_name='发布时间')),
                ('achievement_content', tinymce.models.HTMLField(default='', verbose_name='成果内容')),
                ('publisher', models.CharField(default='', max_length=15, verbose_name='发布人')),
                ('time_size', models.IntegerField(default='', verbose_name='时间先后')),
            ],
        ),
    ]