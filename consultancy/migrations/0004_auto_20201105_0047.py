# Generated by Django 3.1.1 on 2020-11-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultancy', '0003_remove_symptoms_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Skin', 'Skin'), ('Physician', 'Physician'), ('Child issues', 'Child issues')], max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Symptoms',
        ),
    ]
