from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from core.models import BaseModel
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

def user_avatar_upload_path(instance, filename):
    return f"images/perfil-avatar/{instance.username}/{instance.username}-avatar.png"

def user_cover_upload_path(instance, filename):
    return f"images/perfil-cover/{instance.username}/{instance.username}-cover.png"

class MyUserManager(BaseUserManager):
    def create_user(self, email, full_name, username, date_of_birth, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            username=username,
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, username, date_of_birth, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            username=username,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    full_name = models.CharField(max_length=255, verbose_name="full name")
    username = models.CharField(max_length=150, unique=True)
    date_of_birth = models.DateField()
    bio = models.TextField(blank=True, null=True, verbose_name="User bio")
    followers = models.ManyToManyField('self', symmetrical=False, related_name="following", blank=True)
    avatar = models.ImageField(upload_to=user_avatar_upload_path, blank=True, null=True, verbose_name="User Avatar")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    cover = models.ImageField(upload_to=user_cover_upload_path, blank=True, null=True, verbose_name="User Cover")

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "username", "date_of_birth"]

    @property
    def followers_count(self):
        return self.followers.count()

    @property
    def following_count(self):
        return self.following.count()

    @property
    def publications_count(self):
        return self.posts.count() if hasattr(self, 'posts') else 0

    @property
    def favorite_publications_count(self):
        return self.likes.count() if hasattr(self, 'likes') else 0

    @property
    def is_online(self):
        active_sessions = self.sessions.filter(expires_at__gt=timezone.now())
        return active_sessions.exists()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")