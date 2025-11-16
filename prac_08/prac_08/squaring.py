from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """
        Handle calculation (e.g., when the button is pressed),
        and output result to the label widget.
        """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            # Ignore invalid input (e.g., non-numeric text)
            self.root.ids.output_label.text = ''


SquareNumberApp().run()