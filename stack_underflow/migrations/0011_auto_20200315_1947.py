# Generated by Django 2.2.3 on 2020-03-15 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stack_underflow', '0010_auto_20200315_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_underflow.UserProfile', unique=True),
        ),
    ]
