from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lessons.models import SupportedLanguages, SpokenLanguages
from .models import Profile
from .serializers import ProfileSerializer, TeacherProfileSerializer, StudentProfileUpdateSerializer


class ProfilesView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'patch', 'head', 'delete']

    def partial_update(self, request, *args, **kwargs):
        profile_obj = self.get_object()
        data = request.data
        profile_obj.name = data.get('name', profile_obj.name)
        profile_obj.last_name = data.get('last_name', profile_obj.last_name)
        profile_obj.birth_day = data.get('birth_day', profile_obj.birth_day)
        profile_obj.sex = data.get('sex', profile_obj.sex)
        profile_obj.avatar = data.get('avatar', profile_obj.avatar)
        profile_obj.nationality = data.get('nationality', profile_obj.nationality)
        try:
            native_language = SupportedLanguages.objects.get(name=data['native_language'])
            profile_obj.native_language = native_language
        except KeyError:
            pass

        if data["type"] == 'student':
            try:
                for language in data['studied_languages']:
                    studied_languages = SupportedLanguages.objects.filter(name=language)
                    profile_obj.studied_languages.add(*studied_languages)

            except KeyError:
                pass
            profile_obj.save()
            serializer = StudentProfileUpdateSerializer(profile_obj)
            return Response(serializer.data)

        else:
            try:
                language = SupportedLanguages.objects.get(name=data['spoken_languages']['language'])
                level = data['spoken_languages'].get('level')
                spoken_languages = SpokenLanguages.objects.create(
                    user_profile=profile_obj,
                    language=language,
                    level=level
                )
                spoken_languages.save()
            except KeyError:
                pass

            profile_obj.save()
            serializer = TeacherProfileSerializer(profile_obj)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        profile_obj = self.get_object()
        if profile_obj.type == 'student':
            serializer = StudentProfileUpdateSerializer(profile_obj)
            return Response(serializer.data)
        else:
            serializer = TeacherProfileSerializer(profile_obj)
            return Response(serializer.data)

# Проверка запросов:
# Profile.objects.filter()
