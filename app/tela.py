import kivy
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import re

kivy.require('1.11.1')

class Tela(GridLayout):
    tela = ObjectProperty()

    def __init__(self, **kwargs):
        super(Tela, self).__init__(**kwargs)
        self.cols = 1

    def setTextTela(self, txt):
        self.tela.text = txt
        #print(self.tela.text)

    def getCor(self):
        return kivy.utils.get_color_from_hex('#0A5B15')
