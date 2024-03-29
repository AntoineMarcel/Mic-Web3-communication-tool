# Generated by Django 3.2.9 on 2022-04-10 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0006_alter_account_authorized'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Domain',
        ),
        migrations.AlterField(
            model_name='account',
            name='authorized',
            field=models.ManyToManyField(blank=True, to='metadata.Sender'),
        ),
    ]
