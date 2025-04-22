from rest_framework import serializers

from .models import Habit


class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            "id",
            "users",
            "place",
            "time",
            "action",
            "is_nice",
            "related_habit",
            "periodicity",
            "reward",
            "duration",
            "is_public",
        ]
        read_only_fields = ["users"]
