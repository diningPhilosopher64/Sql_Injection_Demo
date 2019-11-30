# Generated by Django 2.2.6 on 2019-11-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descrption', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
