from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    """ User Model Manager """
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError('Users must have email Address')
        if not password:
            raise ValueError('User must have Password')
        # if not full_name:
        #     raise ValueError('User must have a full name')
        user_obj = self.model(
            email=self.normalize_email(email),
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user




class User(AbstractBaseUser):
    
    ROLE = (
        ('staff', 'staff'),
        ('franchise manager', 'franchise manager'),
        ('structure manager', 'structure manager'),
        ('employee', 'employee'),

    )

    # Names
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    # rôles
    role = models.CharField(max_length=100, blank=True, null=True, choices=ROLE)
    # contact
    email = models.EmailField(unique=True)  # require
    number = models.PositiveIntegerField(blank=True, null=True)
    # about
    avatar = models.ImageField(upload_to="icons/avatar", null=True, blank=True)
    # Registration
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Permission
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False, verbose_name="Équipe du Fitness Club")
    is_admin = models.BooleanField(default=False)
    # Main Field for authentication
    USERNAME_FIELD = 'email'



    objects = UserManager()


    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-created_at', '-updated_at', )

    def get_full_name(self):
        if self.first_name:
            return f'{self.first_name}  {self.last_name}'
        return self.email.split('@')[0]
    
        
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True