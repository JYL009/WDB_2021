# Generated by Django 3.2.10 on 2021-12-13 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('memberID', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='아이디')),
                ('nickname', models.CharField(max_length=30, verbose_name='별명')),
                ('password', models.CharField(max_length=15, verbose_name='비밀번호')),
                ('name_mem', models.CharField(max_length=30, verbose_name='사용자명')),
                ('email', models.EmailField(max_length=30, verbose_name='이메일')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='회원가입일자')),
                ('point', models.IntegerField(verbose_name='포인트')),
            ],
            options={
                'db_table': 'MEMBER',
            },
        ),
    ]
