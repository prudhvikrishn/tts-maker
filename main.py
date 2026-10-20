from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.utils import platform
import os

if platform == 'android':
    from jnius import autoclass
    TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
    Locale = autoclass('java.util.Locale')
    Context = autoclass('org.kivy.android.PythonActivity').mActivity

class TTSScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Initialize TTS on Android
        if platform == 'android':
            self.tts = TextToSpeech(Context, None)
            self.languages = {
                "English": Locale.US,
                "Hindi": Locale("hi", "IN"),
                "Telugu": Locale("te", "IN"),
                "French": Locale.FRENCH,
                "German": Locale.GERMAN,
                "Japanese": Locale.JAPANESE
            }
        else:
            self.tts = None
            self.languages = {"English": None}  # Fallback for non-Android testing

        # Text input
        self.add_widget(Label(text="Enter Text:"))
        self.text_input = TextInput(multiline=True, size_hint=(1, 0.4))
        self.add_widget(self.text_input)

        # Language selection
        self.add_widget(Label(text="Language:"))
        self.lang_spinner = Spinner(values=list(self.languages.keys()), text="English")
        self.add_widget(self.lang_spinner)

        # Speed input
        self.add_widget(Label(text="Speed (0.5 to 4.0):"))
        self.speed_input = TextInput(text="1.0", multiline=False)
        self.add_widget(self.speed_input)

        # Convert button
        self.convert_btn = Button(text="Convert & Play", background_color=(0, 0.5, 1, 1))
        self.convert_btn.bind(on_press=self.generate_tts)
        self.add_widget(self.convert_btn)

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

    def generate_tts(self, instance):
        text = self.text_input.text.strip()
        lang = self.languages[self.lang_spinner.text]
        try:
            speed = float(self.speed_input.text)
            if speed < 0.5 or speed > 4.0:
                raise ValueError
        except ValueError:
            self.show_error("Enter speed between 0.5 and 4.0")
            return

        if not text:
            self.show_error("Please enter some text")
            return

        if platform == 'android' and self.tts:
            try:
                self.tts.setLanguage(lang)
                self.tts.setSpeechRate(speed)
                # speak() runs in the background, so the screen stays responsive.
                self.tts.speak(text, TextToSpeech.QUEUE_FLUSH, None)
            except Exception as e:
                self.show_error(f"Error: {str(e)}")
        else:
            self.show_error("TTS only supported on Android")

class TTSApp(App):
    def build(self):
        return TTSScreen()

if __name__ == '__main__':
    TTSApp().run()