from rest_framework import serializers

from lessons.models import SpokenLanguages
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'type', 'avatar', 'sex', 'nationality', 'native_language', 'phone_number', 'birth_day',
                  'name',
                  'last_name']


class SpokenLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpokenLanguages
        fields = ['id', 'level', 'language']


class StudentProfileUpdateSerializer(serializers.ModelSerializer):
    studied_languages = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'type', 'avatar', 'sex', 'nationality', 'native_language', 'birth_day', 'name',
                  'last_name', 'studied_languages']


class TeacherProfileSerializer(serializers.ModelSerializer):
    spoken_languages = SpokenLanguagesSerializer(many=True, required=False)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'type', 'avatar', 'sex', 'nationality', 'native_language', 'birth_day', 'name',
                  'last_name',
                  'spoken_languages']

    def update(self, validated_data):
        spoken_languages = validated_data.pop('spoken_languages')
        profile = Profile.objects.get()
        for language in spoken_languages:
            SpokenLanguages.objects.create(user_profile=profile, **language)
        return profile
