from kivy.app import App
from kivy.uix.textinput import TextInput

class PrveOknoApp(App):
    def build(self):
        return TextInput(hint_text="Sem píš…", font_size="24sp", multiline=False)

PrveOknoApp().run()