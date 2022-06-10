from django.contrib import admin

from .models import SupportedLanguages, Topic, Debate, SpokenLanguages, UserFavouriteTopic, \
    Theme, UserFavouriteDebates, LessonRequest


@admin.register(SupportedLanguages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SpokenLanguages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['language']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'language']
    ordering = ['language', 'level', 'name']


@admin.register(Debate)
class DebateAdmin(admin.ModelAdmin):
    list_display = ['theme', 'name', 'level', 'language']
    ordering = ['language', 'level', 'name', 'theme']


@admin.register(UserFavouriteTopic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic', 'user_profile']


@admin.register(UserFavouriteDebates)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['debate', 'user_profile']


@admin.register(Theme)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(LessonRequest)
class LessonRequestAdmin(admin.ModelAdmin):
    list_display = ['student', 'teacher', 'status', 'type']
