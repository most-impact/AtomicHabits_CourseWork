from rest_framework import generics, permissions

from .models import Habit
from .serializers import HabitSerializers


class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    serializer_class = HabitSerializers
    permission_classes = [permissions.IsAuthenticated]
    queryset = Habit.objects.filter(is_public=True)
