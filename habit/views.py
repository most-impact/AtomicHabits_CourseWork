from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Habit
from .serializers import HabitSerializers


class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializers
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user).order_by('id')


class HabitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    serializer_class = HabitSerializers
    permission_classes = [permissions.IsAuthenticated]
    queryset = Habit.objects.filter(is_public=True)
