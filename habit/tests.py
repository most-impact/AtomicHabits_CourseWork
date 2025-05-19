import unittest
from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from habit.models import Habit
from datetime import time
from django.core.exceptions import ValidationError

User = get_user_model()


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="testuser@example.com", password="testpass")

    @patch("Habit.tasks.send_telegram_reminder.apply_async")
    def test_periodicity_validation(self, mock_task):
        """Тест валидации: периодичность от 1 до 7 дней"""
        with self.assertRaisesMessage(ValidationError, "Переодичность должна быть от 1 до 7 дней"):
            habit = Habit(
                user=self.user,
                place="дома",
                time=time(8, 0),
                action="зарядка",
                is_nice=False,
                periodicity=8,
                duration=60
            )
            habit.save()
        mock_task.assert_not_called()

    @patch("Habit.tasks.send_telegram_reminder.apply_async")
    def test_pleasant_habit_validation(self, mock_task):
        """Тест валидации: у приятной привычки не может быть reward"""
        with self.assertRaisesMessage(ValidationError, "У приятной привычки не может быть вознаграждения или связанной привычки"):
            habit = Habit(
                user=self.user,
                place="дома",
                time=time(9, 0),
                action="принять ванну",
                is_nice=True,
                reward="чай",
                periodicity=1,
                duration=60
            )
            habit.save()
        mock_task.assert_not_called()

    @patch("Habit.tasks.send_telegram_reminder.apply_async")
    def test_habit_reward_and_related_habit_validation(self, mock_task):
        """Тест валидации: нельзя указать и reward, и related_habit"""
        pleasant_habit = Habit(
            user=self.user,
            place="дома",
            time=time(10, 0),
            action="отдых",
            is_nice=True,
            periodicity=1,
            duration=60
        )
        pleasant_habit.save()

        with self.assertRaisesMessage(ValidationError, "Нельзя указывать одновременно вознаграждение и связанную привычку"):
            habit = Habit(
                user=self.user,
                place="парк",
                time=time(7, 0),
                action="прогулка",
                is_nice=False,
                related_habit=pleasant_habit,
                reward="мороженое",
                periodicity=1,
                duration=60
            )
            habit.save()
        mock_task.assert_called_once()

    @patch("Habit.tasks.send_telegram_reminder.apply_async")
    def test_habit_creation_success(self, mock_task):
        """Тест успешного создания привычки с минимальными данными"""
        habit = Habit(
            user=self.user,
            place="офис",
            time=time(12, 0),
            action="обед",
            is_nice=False,
            periodicity=1,
            duration=30
        )
        habit.save()
        self.assertEqual(habit.action, "обед")
        self.assertEqual(habit.place, "офис")
        self.assertEqual(habit.duration, 30)
        self.assertFalse(habit.is_nice)
        self.assertEqual(str(habit), "обед в 12:00:00 в офис")
        mock_task.assert_called_once()


if __name__ == "__main__":
    unittest.main()