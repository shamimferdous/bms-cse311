# Generated by Django 4.0 on 2021-12-28 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0003_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'bill_statuses',
            },
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'months',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateField()),
                ('amount', models.IntegerField()),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.month')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.billstatus')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.subscription')),
            ],
            options={
                'db_table': 'bills',
            },
        ),
    ]
