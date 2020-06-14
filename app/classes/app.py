import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager



kivy.require('1.11.0')


class ScreenControler(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MathApp(App):

    def build(self):
        Builder.load_string(open('app/front/mathapp-front.kv', encoding='utf8').read(), rulesonly=True)

        return ScreenControler()



