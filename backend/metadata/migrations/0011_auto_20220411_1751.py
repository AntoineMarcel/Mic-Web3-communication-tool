# Generated by Django 3.2.9 on 2022-04-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0010_auto_20220411_0808'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sender',
        ),
        migrations.AlterField(
            model_name='account',
            name='authorized',
            field=models.ManyToManyField(blank=True, related_name='_metadata_account_authorized_+', to='metadata.Account'),
        ),
    ]
