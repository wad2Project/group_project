# Generated by Django 2.2.3 on 2020-03-23 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stack_underflow', '0020_auto_20200319_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
