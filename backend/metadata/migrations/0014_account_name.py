# Generated by Django 3.2.9 on 2022-04-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0013_alter_account_authorized'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]