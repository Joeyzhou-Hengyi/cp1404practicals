from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that dynamically creates labels from a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # data/model: list of names
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Lindsay Ward"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from the names list and add them to the main BoxLayout."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


if __name__ == "__main__":
    DynamicLabelsApp().run()