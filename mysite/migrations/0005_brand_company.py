# Generated by Django 5.0 on 2023-12-20 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_brand_category_delete_company_delete_person_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='company',
            field=models.CharField(default='n/a', max_length=100),
        ),
    ]
