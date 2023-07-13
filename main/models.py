from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from thatofinanceapi.thatofinanceapi.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


class LoanApplication(models.Model):
    loan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    loan_type = models.CharField(max_length=100)
    loan_amount = models.CharField(max_length=100)
    loan_term = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Id_number = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    marital_property = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    cell = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dependants = models.IntegerField()
    race = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    length_of_employment = models.IntegerField()
    employee_number = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    emp_telephone = models.CharField(max_length=100)
    emp_email = models.CharField(max_length=100)
    net_income = models.CharField(max_length=100)
    basic_income = models.CharField(max_length=100)
    living_expenses = models.CharField(max_length=100)
    monthly_loan_repayments = models.CharField(max_length=100)
    total_expenses = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    account_holder = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=100)

    def __str__(self):
        return self.loan_amount


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Userprofile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)

    tel = models.CharField(max_length=100)

    is_master = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
