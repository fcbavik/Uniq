from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


from django.db.models.signals import post_save
from django.utils import timezone

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student')
    անուն = models.CharField(max_length=20)
    ազգանուն =  models.CharField(max_length=20)
    մոգ = models.FloatField(default=0)
    # ընդունելություն = models.DateField(default=timezone.now().year)
    ընդունելություն = models.IntegerField(default=timezone.now().year)
    ուսուցման_համակարգ =  models.CharField(max_length=20)
    կրթական_ծրագիր =  models.CharField(max_length=20)
    ֆակուլտետ =  models.CharField(max_length=20)
    մասնագիտություն =  models.CharField(max_length=20)
    կուրս = models.IntegerField(default=1)
    խումբ = models.IntegerField(default=1)
    զեղչ  = models.IntegerField(default=0)

    def __str__(self):
        return self.անուն + " " +  self.ազգանուն

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Student.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
