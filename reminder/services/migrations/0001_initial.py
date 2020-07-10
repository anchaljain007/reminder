# Generated by Django 3.0.8 on 2020-07-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeTaxModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_install_due', models.DateField()),
                ('second_install_due', models.DateField()),
                ('third_install_due', models.DateField()),
                ('fourth_install_due', models.DateField()),
                ('tax_return_date', models.DateField()),
                ('tds_return_date', models.DateField()),
            ],
        ),
    ]