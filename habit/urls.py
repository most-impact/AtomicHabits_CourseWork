from django.urls import path

from .views import UserHabitListAPIView, PublicHabitListAPIView, HabitCreateAPIView, HabitRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("habits/", UserHabitListAPIView.as_view(), name="user-habit-list"),
    path("public-habits/", PublicHabitListAPIView.as_view(), name="public-habit-list"),
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habits/<int:pk>/", HabitRetrieveUpdateDestroyAPIView.as_view(), name="habit-detail"),
]