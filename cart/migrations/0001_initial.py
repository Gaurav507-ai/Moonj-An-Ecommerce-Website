# Generated by Django 4.0.3 on 2022-11-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_name', models.CharField(max_length=50)),
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
