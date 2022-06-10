from django.urls import path
from rest_framework import routers

from .views import RelevantTeachersListView
from .views import TopicView, DebateView, FavouriteTopicsView, FavouriteDebateView, LessonRequestView, \
    SupportedLanguagesView

urlpatterns = [
    path('relevant_teachers', RelevantTeachersListView.as_view()),
    path('supported_languages', SupportedLanguagesView.as_view()),
]

router = routers.DefaultRouter()
router.register(r'topics', TopicView)
router.register(r'debates', DebateView)
router.register(r'favourite_topics', FavouriteTopicsView)
router.register(r'favourite_debates', FavouriteDebateView)
router.register(r'lesson_request', LessonRequestView)

urlpatterns += router.urls
