# Generated by Django 4.0.6 on 2022-08-13 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
