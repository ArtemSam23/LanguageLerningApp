from django.db import models

from dialog_app.models import CustomUser


class Profile(models.Model):
    class TYPES(models.TextChoices):
        student = 'student', 'student'
        teacher = 'teacher', 'teacher'

    type = models.CharField(max_length=255, choices=TYPES.choices, default=TYPES.student)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', blank=True)
    native_language = models.ForeignKey("lessons.SupportedLanguages", on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=255, default='', blank=True)
    name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    birth_day = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True)
    nationality = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
