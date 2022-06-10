from django.db import models

from user_profile.models import Profile


class SupportedLanguages(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Level(models.IntegerChoices):
    BEGINNER = 1, 'A1'
    ELEMENTARY = 2, 'A2'
    INTERMEDIATE = 3, 'B1'
    UPPER_INTERMEDIATE = 4, 'B2'
    ADVANCED = 5, 'C1'
    PROFICIENCY = 6, 'C2'


class SpokenLanguages(models.Model):
    language = models.ForeignKey(SupportedLanguages, on_delete=models.CASCADE, blank=True, null=True)
    level = models.IntegerField(choices=Level.choices, default=Level.BEGINNER)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='spoken_languages')


class Theme(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    language = models.ForeignKey(SupportedLanguages, on_delete=models.CASCADE)
    level = models.IntegerField(choices=Level.choices, default=Level.BEGINNER)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'language')


class Debate(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=30)
    description = models.TextField()
    language = models.ForeignKey(SupportedLanguages, on_delete=models.CASCADE)
    level = models.IntegerField(choices=Level.choices, default=Level.BEGINNER)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'language')


class LessonRequest(models.Model):
    class LessonTypes(models.TextChoices):
        topic = 'topic'
        debate = 'debate'

    class Status(models.TextChoices):
        sent = 'sent'
        accepted = 'accepted'
        declined = 'declined'
        scheduled = 'scheduled'
        started = 'started'
        completed = 'completed'

    timestamp = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='request_student')
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='request_teacher')
    type = models.CharField(max_length=30, choices=LessonTypes.choices)
    status = models.CharField(choices=Status.choices, max_length=10, default=Status.sent)
    topic = models.ManyToManyField(Topic, related_name='request_topics', blank=True)
    debate = models.ManyToManyField(Debate, related_name='request_debates', blank=True)

    def __str__(self):
        return f'Lesson request from {self.student.name} to {self.teacher.name}'


class UserFavouriteTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class UserFavouriteDebates(models.Model):
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
