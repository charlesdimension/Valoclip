# Generated by Django 4.1.1 on 2022-10-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='video',
            name='cheating',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='video',
            name='not_cheating',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.TextField(max_length=40),
        ),
    ]
