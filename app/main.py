import kivy
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import re

kivy.require('1.11.1')

class Keyboard(GridLayout):
    tela = ObjectProperty()

    def __init__(self, **kwargs):
        super(Keyboard, self).__init__(**kwargs)
        self.cols = 4

    def getCor(self):
        return kivy.utils.get_color_from_hex('#0A5B15')

    def teclado(self, info):
        self.tela.text += info

    def apagar(self):
        self.tela.text = self.tela.text[:-1]

    def clean(self):
        self.tela.text = ""

    def incognita(self):
        if len(self.tela.text) > 0:
            if self.tela.text[-1] != 'x':
                self.tela.text += 'x'
            else:
                self.tela.text = self.tela.text[:-1]
                self.tela.text += 'x²'
        else:
            self.tela.text += 'x'

    def soma(self):
        if len(self.tela.text) > 0:
            if self.tela.text[-1] == '-':
                self.tela.text = self.tela.text[:-1]
                self.tela.text += ' + '
            elif self.tela.text[-1] == '+':
                self.tela.text = self.tela.text[:-1]
                self.tela.text += ' - '
            else:
                self.tela.text += ' + '
        else:
            self.tela.text += ' + '

    def virgula(self):
        if ',' in self.tela.text.split('+')[-1]:
            if self.tela.text[-1] == ',':
                return
        else:
            self.tela.text += ','

    def validate(self):
        exp_a = re.compile('([-]?\d+)(?=[a-zA-Z]\²)')
        exp_b = re.compile('-?\d+(?![a-zA-Z]\^)(?=[a-zA-Z])')
        exp_c = re.compile('-?\d+')

        a = (exp_a.match(self.tela.text).group())
        b = (exp_b.match(self.tela.text).group())
        c = (exp_c.match(self.tela.text).group())

        if a != 0:
            self.tela.text = "Válido   a = " + a + ", b = " + b + " e c = " + c
        else:
            self.tela.text = "Inválido"

class MathApp(App):

    def build(self):
        Builder.load_string(open('mathapp-front.kv', encoding='utf8').read(), rulesonly=True)
        return Keyboard()


MathApp().run()
