from textual.widgets import Input, Label, Select, Button
from textual.widget import Widget
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.events import Event

PRIORITIES = ["HIGH", "MEDIUM", "LOW"]

class TaskBuilder(Widget):
	def __init__(self, add_task_callback):
		super().__init__()
		self.add_task_callback = add_task_callback  # Store callback function

	def compose(self) -> ComposeResult:
		self.task_name = Input(placeholder="Task Name")
		self.priority = Select([(p, p) for p in PRIORITIES])
		self.due_label = Label("Due")
		self.due_date = Input(placeholder="DD:MM:YYYY")
		self.create_button = Button("Create", id="create_task")

		yield Vertical(
			self.task_name,
			self.priority,
			self.due_label,
			self.due_date,
			self.create_button
		)

	def on_button_pressed(self, event: Button.Pressed) -> None:
		if event.button.id == "create_task":
			title = self.task_name.value.strip()
			priority = self.priority.value or "MEDIUM"  # Default priority
			due_date = self.due_date.value.strip()

			if title:  # Ensure task has a name
				self.add_task_callback(title, priority, due_date)  # Call the callback
				self.remove()  # Close TaskBuilder after adding task

class Task:
	def __init__(self, task_id, title, age, description, priority, due):
		self.task_id = task_id
		self.title = title
		self.age = age
		self.description = description
		self.priority = priority
		self.due = due

	def __repr__(self):
		return f"Task({self.task_id}, {self.title}, {self.priority}, {self.due})"

