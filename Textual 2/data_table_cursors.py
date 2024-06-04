from textual.app import App, ComposeResult
from textual.widgets import DataTable
from textual.binding import Binding
from textual.containers import Horizontal
from textual.widgets import Footer
from textual.screen import Screen


ROWS = [
    ("ID", "Nombre"),
    (1, "Yoel"),
    (4, "Samuel"),
    (7, "Amaro")
]


class TableApp(App):

    BINDINGS = [
        Binding(key="E", action="3", description="Editar"),
        Binding(key="N", action="4", description="Crear"),
        Binding(key="H", action="5", description="Borrar"),
        Binding(key="Q", action="quit", description="Salir")
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

class ModesApp(App):
    BINDINGS = [
        ("m", "switch_mode('main')", "Principal"),  
        ("e", "switch_mode('edit')", "Edición"),
    ]
    MODES = {
        "main": MainScreen,  
        "edit": EditScreen
    }

    def on_mount(self) -> None:
        self.switch_mode("main")  


app = TableApp()
if __name__ == "__main__":
    app.run()