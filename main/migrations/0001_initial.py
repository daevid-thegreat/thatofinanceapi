# Generated by Django 4.2.3 on 2023-07-15 13:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('loan_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=100)),
                ('loan_amount', models.CharField(max_length=100)),
                ('loan_term', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('Id_number', models.CharField(max_length=100)),
                ('marital_status', models.CharField(max_length=100)),
                ('marital_property', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('cell', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('dependants', models.IntegerField()),
                ('race', models.CharField(max_length=100)),
                ('employer', models.CharField(max_length=100)),
                ('length_of_employment', models.IntegerField()),
                ('employee_number', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('emp_telephone', models.CharField(max_length=100)),
                ('emp_email', models.CharField(max_length=100)),
                ('net_income', models.CharField(max_length=100)),
                ('basic_income', models.CharField(max_length=100)),
                ('living_expenses', models.CharField(max_length=100)),
                ('monthly_loan_repayments', models.CharField(max_length=100)),
                ('total_expenses', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=100)),
                ('account_holder', models.CharField(max_length=100)),
                ('branch_code', models.CharField(max_length=100)),
                ('status', models.CharField(default='Pending', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
