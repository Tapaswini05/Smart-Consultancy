# Generated by Django 3.1.1 on 2020-11-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultancy', '0005_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('category', models.CharField(choices=[('Skin', 'Skin'), ('Physician', 'Physician'), ('Child issues', 'Child issues'), ('Gynaecologist', 'Gynaecologist'), ('Dermatologist', 'Dermatologist')], max_length=200, null=True)),
            ],
        ),
    ]
