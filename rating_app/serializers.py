from rest_framework import serializers

from rating_app.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class TeacherRatingSerializer(serializers.Serializer):
    rating = serializers.FloatField()
    teacher_id = serializers.IntegerField()
