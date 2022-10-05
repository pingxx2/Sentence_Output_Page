# Generated by Django 3.2.16 on 2022-10-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='문구')),
                ('title', models.CharField(max_length=300, verbose_name='제목')),
                ('writer', models.CharField(max_length=100, verbose_name='작성자')),
            ],
        ),
    ]
