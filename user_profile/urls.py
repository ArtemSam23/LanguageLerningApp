from rest_framework import routers
from .views import ProfilesView
from django.urls import include, path, re_path

router = routers.DefaultRouter()
router.register(r'profile', ProfilesView, basename='Profile')
urlpatterns = router.urls

#urlpatterns = [path('profile/<int:pk>', ProfilesView),]
