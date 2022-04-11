# Generated by Django 3.2.9 on 2022-04-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0003_alter_account_authorized'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='authorized',
        ),
        migrations.AddField(
            model_name='account',
            name='authorized',
            field=models.ManyToManyField(to='metadata.Domain'),
        ),
    ]
