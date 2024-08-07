# Generated by Django 5.0.4 on 2024-05-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('emp_id', models.IntegerField()),
                ('salary', models.FloatField()),
                ('active_emp', models.BooleanField(default=True)),
                ('joined_date', models.DateField()),
                ('last_updated', models.DateTimeField()),
            ],
        ),
    ]
