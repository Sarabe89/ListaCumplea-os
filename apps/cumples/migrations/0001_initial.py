# Generated by Django 4.2.7 on 2023-11-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cumpleañero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('date_bord', models.DateField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='cumpleañeros/')),
            ],
            options={
                'verbose_name': 'Cumpleañero',
                'verbose_name_plural': 'Cumpleañeros',
            },
        ),
    ]