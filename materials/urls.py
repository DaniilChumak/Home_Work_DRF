from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateApiView,
                             LessonDestroyApiView, LessonListApiView,
                             LessonReviewAPIView, LessonUpdateApiView, SubscriptionCreateAPIView)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet, basename="course")

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lesson-list"),
    path('lesson/<int:pk>/', LessonReviewAPIView.as_view(),name='lesson_review'),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson-create"),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson-delete"),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson-update"),
    path('course_subscription/', SubscriptionCreateAPIView.as_view(),name='course_subscription'),
]

urlpatterns += router.urls
