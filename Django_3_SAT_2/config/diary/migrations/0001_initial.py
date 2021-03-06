# Generated by Django 2.2.9 on 2020-01-18 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='열기 제목', max_length=20, verbose_name='일기 제목')),
                ('content', models.TextField(help_text='일기내용', verbose_name='일기내용')),
                ('image', models.ImageField(help_text='일기 이미지', upload_to='images', verbose_name='일기 이미지')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='작성일', verbose_name='작성일')),
            ],
        ),
    ]
