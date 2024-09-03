from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateApiView,
                             LessonDestroyApiView, LessonListApiView,
                             LessonRetrieveApiView, LessonUpdateApiView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet, basename="course")

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lesson-list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson-retrieve"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson-create"),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson-delete"),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson-update"),
]

urlpatterns += router.urls
