from django.contrib import admin

from rating_app.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['student', 'lesson', 'star']
