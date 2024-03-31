from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App which shows dynamic labels"""

    def __init__(self):
        """Initialize a list of names"""
        super().__init__()
        self.names = ["John", "Linda", "Max", "Natsu"]

    def build(self):
        """Build the Kivy app from kivy file"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
