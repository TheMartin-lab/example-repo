#joshua Martin
#OOP
#JO25080018810
import unittest
from src.business_logic import TaskService, Task
from src.in_memory_repository import InMemoryTaskRepository


class TestTaskService(unittest.TestCase):
    """Unit tests for the TaskService class."""

    def setUp(self):
        """
        Arrange:
        Set up the necessary objects and conditions for every test.
        Create an instance of TaskService using the in-memory repository.
        """
        self.repo = InMemoryTaskRepository()
        self.task_service = TaskService(self.repo)

    def test_add_task(self):
        """Test the add_task method of TaskService."""
        # Arrange
        initial_task_count = len(self.task_service.get_all_tasks())
        new_task = Task(
            title="New Task",
            description="Description of the new task"
        )

        # Act
        self.task_service.add_task(new_task)

        # Assert
        updated_task_count = len(self.task_service.get_all_tasks())
        self.assertEqual(
            updated_task_count,
            initial_task_count + 1
        )
        self.assertIn(new_task, self.task_service.get_all_tasks())

    def test_add_task_empty_title_raises(self):
        """Test that adding a task with an empty title raises a ValueError."""
        # Arrange
        invalid_task = Task(title="", description="No title")

        # Act + Assert
        with self.assertRaises(ValueError):
            self.task_service.add_task(invalid_task)


if __name__ == "__main__":
    unittest.main()
