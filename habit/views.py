from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from .pagination import CustomHabitPagination
from .serializers import HabitSerializers
from .models import Habit


class UserHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = CustomHabitPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializers
    pagination_class = CustomHabitPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = CustomHabitPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

