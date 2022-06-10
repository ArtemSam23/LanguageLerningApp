from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from lessons.filters import RelevantTeacherFilterBackend
from user_profile.models import Profile
from user_profile.serializers import TeacherProfileSerializer
from .models import Topic, Debate, SupportedLanguages
from .models import UserFavouriteDebates, UserFavouriteTopic, LessonRequest
from .serializers import TopicSerializer, SupportedLanguagesSerializer, \
    UsersTopicFavouriteSerializer, UsersDebateFavouriteSerializer, \
    LessonRequestCreateSerializer, LessonRequestRetrieveSerializer


class SupportedLanguagesView(generics.ListAPIView):
    serializer_class = SupportedLanguagesSerializer
    queryset = SupportedLanguages.objects.all()


class TopicView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = (IsAuthenticated,)


class DebateView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TopicSerializer
    queryset = Debate.objects.all()
    permission_classes = (IsAuthenticated,)


class FavouriteTopicsView(viewsets.ModelViewSet):
    serializer_class = UsersTopicFavouriteSerializer
    queryset = UserFavouriteTopic.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete']


class FavouriteDebateView(viewsets.ModelViewSet):
    serializer_class = UsersDebateFavouriteSerializer
    queryset = UserFavouriteDebates.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'delete']


class RelevantTeachersListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = TeacherProfileSerializer
    filter_backends = [RelevantTeacherFilterBackend]


class LessonRequestView(viewsets.ModelViewSet):
    queryset = LessonRequest.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return LessonRequestRetrieveSerializer
        return LessonRequestCreateSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user.profile)
