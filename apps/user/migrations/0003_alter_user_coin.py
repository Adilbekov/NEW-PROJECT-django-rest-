# Generated by Django 5.0.1 on 2024-01-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='coin',
            field=models.SmallIntegerField(blank=True, default=4, null=True, verbose_name='Gik-Coin(ученика)'),
        ),
    ]
