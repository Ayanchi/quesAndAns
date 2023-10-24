# Generated by Django 4.2.6 on 2023-10-17 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TimeField(max_length=400)),
                ('answer', models.TimeField(max_length=600)),
                ('site_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
        ),
    ]