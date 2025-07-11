from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

TIPOS_USUARIO = (
    ('usuario', 'Usuário Comum'),
    ('analista', 'Analista'),
)

class UsuarioManager(BaseUserManager):
    def create_user(self, email, senha=None, **extra_fields):
        if not email:
            raise ValueError('O campo email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, senha, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    setor_id = models.IntegerField(null=True, blank=True)
    cargo_id = models.IntegerField(null=True, blank=True)
    grupo_ids = models.JSONField(default=list, blank=True)

    tipo = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='usuario')
    ultimo_acesso = models.DateTimeField(null=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    deletado = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'tipo']

    objects = UsuarioManager()

    def __str__(self):
        return self.nome or self.email
