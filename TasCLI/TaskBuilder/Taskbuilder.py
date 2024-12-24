from textual.widgets import Input, Label
from textual.widget import Widget
from textual.app import ComposeResult
from textual.containers import Vertical
class TaskBuilder(Widget):
	def compose(self) -> ComposeResult:
		yield Vertical(
				Input(placeholder="Task Name"),
				Input(placeholder="Priority"),
				Label("Due"),
				Input(placeholder="DD:MM:YYYY")
		)
