# Generated by Django 4.1.4 on 2023-01-03 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_remove_photo_announcement_delete_announcement_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Primaire', 'Primaire'), ('Collège', 'Collège'), ('Lycée', 'Lycée')], max_length=50, null=True)),
                ('theme', models.CharField(max_length=50, null=True)),
                ('modality', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=200, null=True)),
                ('rate', models.FloatField()),
                ('wilaya', models.CharField(max_length=50, null=True)),
                ('commune', models.CharField(max_length=50, null=True)),
                ('adresse', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('announcer', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
