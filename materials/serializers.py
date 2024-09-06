from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    count_of_lessons = serializers.SerializerMethodField()
    lessons_info = serializers.SerializerMethodField()

    @staticmethod
    def get_number_of_lessons(obj):
        return obj.count_of_lessons

    def get_lessons_info(obj):
        return LessonSerializer(obj.lessons_info.all(), many=True).data

    class Meta:
        model = Course
        """Выводим все поля, добавляя поле количества уроков"""
        fields = ("title", "description", "preview_image", "count_of_lessons")


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
