from textual.app import App, ComposeResult
from textual.widgets import Input, ListView, ListItem, TextArea, Footer, Label
from textual.containers import Horizontal, Vertical, Center
from textual.binding import Binding

from TaskBuilder.Taskbuilder import TaskBuilder, Task
from datetime import datetime

class TasCLI(App):
	LIST = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
	TASKS = []
	task_builder = None
	default_task = Task(0, "Default", datetime.now(), "", "MEDIUM", "now")
	TASKS.append(default_task)
	
	BINDINGS = [
		Binding('q', 'quit()', 'quit'),
		Binding('a', 'add_task()', 'add task'),
		Binding('d', 'delete_task()', 'delete task'),
	]

	def action_quit(self) -> None:
		self.exit()

	def add_new_task(self, title: str, priority: str, due_date: str) -> None:
		task_id = len(self.TASKS) + 1
		new_task = Task(task_id, title, datetime.now(), "", priority, due_date)
		self.TASKS.append(new_task)
		self.list_view.mount(ListItem(Label(title)))
		
		if (self.task_builder):
			self.task_builder.remove()
			self.task_builder = None

	def action_add_task(self) -> None:
		if (self.task_builder is None):
			task_builder = TaskBuilder(self.add_new_task)
			self.mount((task_builder))

	def compose(self) -> ComposeResult:
		self.list_view = ListView(
			*[ListItem(Label(item.title)) for item in self.TASKS]
		)
		search_box = Input(placeholder="Search Task")
		yield Horizontal(
			Vertical(
				search_box,
				self.list_view
			),
			TextArea()
		)
		yield Footer()

	async def on_input_changed(self, event: Input.Changed) -> None:
		search_string = event.value.lower()
		filtered = [item.title for item in self.TASKS if search_string in item.title.lower()]
		self.list_view.clear()
		self.list_view.mount_all([ListItem(Label(item)) for item in filtered])

if __name__ == "__main__":
	app = TasCLI()
	app.run()
