# Generated by Django 3.0.8 on 2020-10-27 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201027_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('SPORTS', 'Sports'), ('ELECTRONICS', 'Electronics'), ('FASHION', 'Fashion'), ('TOYS', 'Toys'), ('HOME', 'Home'), ('MISCELLANEOUS', 'Miscellaneous')], default='Category not specified.', max_length=64),
        ),
    ]
