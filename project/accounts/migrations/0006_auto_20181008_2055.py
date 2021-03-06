# Generated by Django 2.1.1 on 2018-10-08 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_shift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='pdf_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdf', to='accounts.PDFFile'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
