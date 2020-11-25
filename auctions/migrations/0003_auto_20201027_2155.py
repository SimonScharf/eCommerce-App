# Generated by Django 3.0.8 on 2020-10-27 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Sports', 'sports'), ('Electronics', 'electronics'), ('Fashion', 'fashion'), ('Toys', 'toys'), ('Home', 'home'), ('Miscellaneous', 'miscellaneous')], default='Category not specified.', max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_link',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]
