from django.urls import path
from rest_framework import routers

from rating_app.views import RatingView, TeacherRatingView

urlpatterns = [
    path('teachers_rating', TeacherRatingView.as_view()),
]

router = routers.DefaultRouter()
router.register(r'rating', RatingView)

urlpatterns += router.urls
