from rest_framework import filters


class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)


class RelevantTeacherFilterBackend(filters.BaseFilterBackend):
    """
    Filter teachers by languages, level, age
    """
    aliases = {
        'lang_code': 'spoken_languages__language__code',
        'level': 'spoken_languages__level__gte',
    }

    def filter_queryset(self, request, queryset, view):
        queryset = queryset.filter(type='teacher')
        for query_param in request.query_params.keys():
            queryset = queryset.filter(**{self.aliases[query_param]: request.query_params.get(query_param)})
        return queryset
