from textual.app import App, ComposeResult
from textual.widgets import Input
from textual.containers import Horizontal
from textual.widgets import Button
from textual.widgets import DataTable


class Screen(App):
    def compose(self) -> ComposeResult:
         yield Input(placeholder="Nombre")
         yield Horizontal(
                Button("Aceptar"),
                Button("Cancelar")
        )

app = TableApp()
if __name__ == "__main__":
    app.run()