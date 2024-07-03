
from django.urls import path, include

from .views import DepartmentViewSet, PersonViewSet



from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("department", DepartmentViewSet)  # categories/ categories/<int:pk>/
router.register("person", PersonViewSet)  # categories/ categories/<int:pk>/


urlpatterns = [
     path("", include(router.urls))
]
