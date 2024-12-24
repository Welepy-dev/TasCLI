from textual.app import App, ComposeResult
from textual.widgets import Input, ListView, ListItem, TextArea, Footer, Label
from textual.containers import Horizontal, Vertical
from textual.events import Key
from textual.binding import Binding

from TaskBuilder.Taskbuilder import TaskBuilder


class Task:
	def __init__(self, identification, title, age, description, priority, due):
		...
class TasCLI(App):
	LIST = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
	TASKS = []
	BINDINGS = [
			Binding('q', 'quit()', 'quit'),
			Binding('a', 'add_task()', 'add task'),
			Binding('d', 'delete_task()', 'delete task'),
	]
	def action_quit(self) -> None:
		self.exit()
	def action_add_task(self) -> None:
		task_builder = TaskBuilder()
		self.mount(task_builder)
	def compose(self) -> ComposeResult:
		self.list_view = ListView(
				*[ListItem(Label(item)) for item in self.LIST]
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
		filtered = [item for item in self.LIST if search_string in item.lower()]
		self.list_view.clear()
		self.list_view.mount_all([ListItem(Label(item)) for item in filtered])
	#async def on_key(self, event: Key) -> None:
	#	if (event.Key == ''
if __name__ == "__main__":
    app = TasCLI()
    app.run()
