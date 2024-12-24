from textual.app import App, ComposeResult
from textual.widgets import Input, ListView, ListItem, TextArea, Label
from textual.containers import Horizontal, Vertical

class TasCLI(App):
	LIST = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
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

	async def on_input_changed(self, event: Input.Changed) -> None:
		search_string = event.value.lower()
		filtered = [item for item in self.LIST if search_string in item.lower()]
		self.list_view.clear()
		self.list_view.mount_all([ListItem(Label(item)) for item in filtered])
if __name__ == "__main__":
    app = TasCLI()
    app.run()
