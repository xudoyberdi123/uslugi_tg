# Generated by Django 3.2.7 on 2021-09-13 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
        ('tg', '0007_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.JSONField(blank=True, default={'from': 0, 'to': 0}, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(related_name='announce_category', to='tg.Category')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.region')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tg.user')),
            ],
        ),
    ]
