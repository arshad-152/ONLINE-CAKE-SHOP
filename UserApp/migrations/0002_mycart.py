# Generated by Django 5.1 on 2024-09-24 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=20)),
                ('cake', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AdminApp.cake')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserApp.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]
