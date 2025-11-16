from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Simple app to demonstrate BoxLayout with greet and clear actions."""

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        """Greet the user using the text from the input field."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Clear the input field and the output label."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()