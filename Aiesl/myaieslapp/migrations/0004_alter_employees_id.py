# Generated by Django 4.1.5 on 2023-02-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaieslapp', '0003_alter_arrivalschedule_id_alter_departureschedule_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]