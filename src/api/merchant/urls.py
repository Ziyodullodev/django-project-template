from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.include_root_view = False

urlpatterns = [

    path('', include(router.urls))
]
