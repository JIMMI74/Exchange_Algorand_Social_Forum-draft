# Generated by Django 4.0.2 on 2022-03-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_profile_algo_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ALGO_Wallet',
            field=models.FloatField(default=5),
        ),
    ]
