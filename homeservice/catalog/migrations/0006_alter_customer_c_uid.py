# Generated by Django 4.0.5 on 2022-07-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_customer_c_uid_alter_worker_w_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='c_uid',
            field=models.EmailField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
