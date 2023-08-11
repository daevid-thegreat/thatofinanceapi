# Generated by Django 3.2.20 on 2023-08-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_loanapplication_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='bank_statement',
            field=models.FileField(default=None, upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='id_document',
            field=models.FileField(default=None, upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='payslip',
            field=models.FileField(default=None, upload_to='documents/'),
            preserve_default=False,
        ),
    ]
