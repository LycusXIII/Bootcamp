# Generated by Django 5.0.6 on 2024-07-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]