from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static
from textual.binding import Binding
from textual.widgets import Footer


class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    BINDINGS = [
        Binding(key="q", action="quit", description="Salir")
    ]

    def compose(self) -> ComposeResult:

        yield Horizontal(
            VerticalScroll(
                Static("Llamar a Pepe", classes="header"),
                Button("Llamar", id="butLlamar")
            ),
        )

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        
        if event.button.id == "butLlamar":
            self.notify(
                "Está llamando"
                "[b] A Pepe",
                title="Llamada",
                severity="warning",
            )
        


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())
    
    