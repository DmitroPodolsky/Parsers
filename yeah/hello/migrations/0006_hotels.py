# Generated by Django 4.1.3 on 2022-12-13 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_delete_hotels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]