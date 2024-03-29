# Generated by Django 5.0 on 2024-01-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('pdf', models.FileField(upload_to='books/pdf')),
                ('cover', models.FileField(blank=True, null=True, upload_to='books/cover')),
            ],
        ),
    ]
