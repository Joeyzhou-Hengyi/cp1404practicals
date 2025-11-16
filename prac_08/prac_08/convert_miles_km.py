from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

MILES_TO_KM = 1.60934


class MilesConverter(BoxLayout):
    """Root widget of the app."""
    output_km = StringProperty("0.0")


class MilesConverterApp(App):
    """App for converting miles to kilometres."""

    def build(self):
        """Load the UI from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Calculate miles to kilometres and update the output label."""
        miles = self.get_validated_miles()
        result = miles * MILES_TO_KM
        self.root.output_km = str(result)

    def handle_increment(self, change):
        """Increase or decrease the miles input."""
        miles = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        """Return the miles value as float, or 0.0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


if __name__ == '__main__':
    MilesConverterApp().run()
