from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static


class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    def compose(self) -> ComposeResult:

        yield Horizontal(
            VerticalScroll(
                Static("Llamar a Pepe", classes="header"),
                Button("Llamar", id="butLlamar"),
                Button.error("Salir", id="butSalir")
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "butSalir":
            self.exit(str(event.button))
        elif event.button.id == "butLlamar":
            self.notify(
                "Está llamando"
                "[b] A Pepe",
                title="Llamada",
                severity="warning",
            )


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())