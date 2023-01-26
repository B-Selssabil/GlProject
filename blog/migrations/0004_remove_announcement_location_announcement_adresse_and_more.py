# Generated by Django 4.1.4 on 2023-01-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_adress_announcer_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='location',
        ),
        migrations.AddField(
            model_name='announcement',
            name='adresse',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='commune',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='announcement',
            name='wilaya',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]