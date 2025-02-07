from textual.app import App, ComposeResult
from textual.widgets import Input, ListView, ListItem, TextArea, Footer, Label
from textual.containers import Horizontal, Vertical, Center
from textual.binding import Binding

from TaskBuilder.Taskbuilder import TaskBuilder, Task
from datetime import datetime

class TasCLI(App):
    LIST = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    TASKS = []
    
    BINDINGS = [
        Binding('q', 'quit()', 'quit'),
        Binding('a', 'add_task()', 'add task'),
        Binding('d', 'delete_task()', 'delete task'),
    ]

    def action_quit(self) -> None:
        """Quit the app."""
        self.exit()

    def add_new_task(self, title: str, priority: str, due_date: str) -> None:
        """Callback function to receive tasks from TaskBuilder."""
        task_id = len(self.TASKS) + 1
        new_task = Task(task_id, title, datetime.now(), "", priority, due_date)
        self.TASKS.append(new_task)
        
        # Add to the ListView dynamically
        self.list_view.mount(ListItem(Label(title)))

    def action_add_task(self) -> None:
        """Open TaskBuilder in a centered box."""
        task_builder = TaskBuilder(self.add_new_task)  # Pass callback function
        self.mount(Center(task_builder))
        task_builder.focus()

    def compose(self) -> ComposeResult:
        """Layout of the app."""
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
        """Filter tasks based on search input."""
        search_string = event.value.lower()
        filtered = [item for item in self.LIST if search_string in item.lower()]
        self.list_view.clear()
        self.list_view.mount_all([ListItem(Label(item)) for item in filtered])

if __name__ == "__main__":
    app = TasCLI()
    app.run()

