# -*- encoding: utf-8 -*-
import kivy.utils
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout


class Tela(GridLayout):
    display = ObjectProperty()
    information = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

    def set_text(self, txt):
        self.display.text = txt

    def get_text(self):
        return self.display.text

    def append_text(self, txt):
        self.display.text += txt

    def remove(self, qtd=1):
        self.display.text = self.display.text[:qtd * -1]

    def get_cor(self):
        return kivy.utils.get_color_from_hex('#0A5B15')

    def change_info(self, text):
        self.information.text = text
