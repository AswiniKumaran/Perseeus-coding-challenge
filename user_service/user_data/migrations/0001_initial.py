# Generated by Django 2.2 on 2020-03-15 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('lastName', models.CharField(max_length=20)),
                ('firstName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=20, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mobile', to='user_data.User')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_email', to='user_data.User')),
            ],
        ),
    ]