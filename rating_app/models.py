from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from lessons.models import LessonRequest
from user_profile.models import Profile


class Rating(models.Model):
    """Lessons Rating & Review"""
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        LessonRequest,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    star = models.SmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    review = models.TextField(blank=True, null=True)
