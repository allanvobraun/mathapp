#-*- encoding: utf-8 -*-
import kivy
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, Clock
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import re

kivy.require('1.11.1')


class Tela(GridLayout):
    display = ObjectProperty()
    info = ObjectProperty()

    def __init__(self, **kwargs):
        super(Tela, self).__init__(**kwargs)
        self.cols = 1

    def set_text(self, txt):
        self.display.text = txt

    def get_text(self):
        return self.display.text

    def append_text(self, txt):
        self.display.text += txt
    
    def remove(self, qtd=1):
        self.display.text = self.display.text[:qtd*-1]

    def get_cor(self):  # TODO: mudar para snake case
        return kivy.utils.get_color_from_hex('#0A5B15')

    def change_info(self, text):
        self.info.text = text

