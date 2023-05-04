
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.gis.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, name, password=None):
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not name:
            raise ValueError('Users must have a name')

        user = self.model(
            phone_number=self.normalize_phone_number(phone_number),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password):
        user = self.create_user(
            phone_number=phone_number,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def normalize_phone_number(self, phone_number):
        """
        Normalize the phone number by removing non-numeric characters.
        """
        return ''.join(c for c in phone_number if c.isdigit())

class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Akshaya(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    services = models.ManyToManyField(Service)
    is_full = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name}"

