from django.urls import path

from .views import (HabitListCreateView, HabitRetrieveUpdateDestroyView,
                    PublicHabitListView)

urlpatterns = [
    path("habits/", HabitListCreateView.as_view(), name="habit-list-create"),
    path(
        "habits/<int:pk>/",
        HabitRetrieveUpdateDestroyView.as_view(),
        name="habit-detail",
    ),
    path("public-habits/", PublicHabitListView.as_view(), name="public-habits"),
]
