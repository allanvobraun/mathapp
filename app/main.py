import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionGroup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require('1.11.1')


class TopBar(BoxLayout):

    def __init__(self, **kwargs):
        super(TopBar, self).__init__(**kwargs)

    def get_image(self):
        return "/home/allanbraun/PycharmProjects/mathapp/assets/images/baseline_menu_white_48.png"


class MathApp(App):

    def build(self):
        return TopBar()


MathApp().run()
