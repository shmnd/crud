# Generated by Django 5.0.4 on 2024-04-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=25)),
                ('sage', models.IntegerField()),
                ('splace', models.CharField(max_length=25)),
                ('smajor', models.CharField(max_length=10)),
            ],
        ),
    ]
