# Generated by Django 4.2.3 on 2023-07-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortune', '0002_fortune_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fortune',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='fortune',
            name='message',
        ),
        migrations.AddField(
            model_name='fortune',
            name='messages',
            field=models.CharField(default='Default Message', max_length=200),
        ),
        migrations.AddField(
            model_name='fortune',
            name='messages2',
            field=models.CharField(default='Default Message', max_length=200),
        ),
        migrations.AddField(
            model_name='fortune',
            name='xnumber',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='fortune',
            name='ynumber',
            field=models.IntegerField(default=1),
        ),
    ]
