from django.contrib import admin
from .models import Profile
from lessons.models import SpokenLanguages


class SpokenLanguagesInline(admin.TabularInline):
    model = SpokenLanguages


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    inlines = [SpokenLanguagesInline, ]


admin.site.register(Profile, ProfileAdmin)
