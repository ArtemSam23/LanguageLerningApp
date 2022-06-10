from rest_framework import serializers

from .models import Topic, Debate, UserFavouriteTopic, UserFavouriteDebates, LessonRequest, SupportedLanguages


class SupportedLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportedLanguages
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'description']


class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields = ['id', 'theme', 'name', 'description']


class UsersTopicFavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavouriteTopic
        fields = ['id', 'topic', 'user_profile']


class UsersDebateFavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavouriteDebates
        fields = ['id', 'debate', 'user_profile']


class LessonRequestCreateSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(many=True, queryset=Topic.objects.all())
    debate = serializers.PrimaryKeyRelatedField(many=True, queryset=Debate.objects.all())

    class Meta:
        model = LessonRequest
        exclude = ['student', 'status']


class LessonRequestRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonRequest
        fields = '__all__'
        depth = 1
