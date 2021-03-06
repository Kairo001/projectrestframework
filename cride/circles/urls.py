""" Urls de Circles. """

#Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import circles as circles_views

router = DefaultRouter()
router.register(r'circles', circles_views.CircleViewSet, basename='circles')

urlpatterns = [
    path('', include(router.urls))
]