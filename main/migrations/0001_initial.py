# Generated by Django 2.1.4 on 2018-12-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pokeinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokename', models.CharField(blank=True, max_length=10, null=True)),
                ('pokerate', models.CharField(blank=True, max_length=10, null=True)),
                ('waza1', models.CharField(blank=True, max_length=10, null=True)),
                ('waza2', models.CharField(blank=True, max_length=10, null=True)),
                ('waza3', models.CharField(blank=True, max_length=10, null=True)),
                ('waza4', models.CharField(blank=True, max_length=10, null=True)),
                ('waza5', models.CharField(blank=True, max_length=10, null=True)),
                ('waza6', models.CharField(blank=True, max_length=10, null=True)),
                ('waza7', models.CharField(blank=True, max_length=10, null=True)),
                ('waza8', models.CharField(blank=True, max_length=10, null=True)),
                ('waza9', models.CharField(blank=True, max_length=10, null=True)),
                ('waza10', models.CharField(blank=True, max_length=10, null=True)),
                ('waza11', models.CharField(blank=True, max_length=10, null=True)),
                ('waza12', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate1', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate2', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate3', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate4', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate5', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate6', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate7', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate8', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate9', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate10', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate11', models.CharField(blank=True, max_length=10, null=True)),
                ('wazarate12', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
