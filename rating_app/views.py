from django.db.models import Avg, F
from rest_framework import viewsets, generics

from rating_app.models import Rating
from rating_app.serializers import RatingSerializer, TeacherRatingSerializer


class RatingView(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class TeacherRatingView(generics.ListAPIView):
    """Teachers ratings"""
    serializer_class = TeacherRatingSerializer

    def get_queryset(self):
        return Rating.objects.values('lesson__teacher') \
            .annotate(rating=Avg('star')).order_by('rating') \
            .annotate(teacher_id=F('lesson__teacher'))
