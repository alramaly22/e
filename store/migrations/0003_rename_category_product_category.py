# Generated by Django 5.1.3 on 2024-11-15 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_product_is_sale_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]
