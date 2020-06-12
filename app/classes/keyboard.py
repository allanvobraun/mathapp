# -*- encoding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
import re

kivy.require('1.11.1')


class Keyboard(GridLayout):

    def __init__(self, **kwargs):
        super(Keyboard, self).__init__(**kwargs)
        self.cols = 4
        self.master = App.get_running_app()  # Widget pai de todos

    def getCor(self):
        return kivy.utils.get_color_from_hex('#0A5B15')

    def get_teclado(self):
        return self.master.root.get_screen('calculadora').get_child('Tela')

    def teclado(self, text):
        self.get_teclado().display.text += text

    def apagar(self):
        if self.get_teclado().display.text[-1] == " ":
            self.get_teclado().display.text = self.get_teclado().display.text[:-3]
        else:
            self.get_teclado().display.text = self.get_teclado().display.text[:-1]

    def clean(self):
        self.get_teclado().display.text = ""

    def incognita(self):
        if len(self.get_teclado().display.text) > 0:
            if self.get_teclado().display.text[-1] != 'x':
                self.get_teclado().display.text += 'x'
            else:
                self.get_teclado().display.text = self.get_teclado().display.text[:-1]
                self.get_teclado().display.text += 'x²'
        else:
            self.get_teclado().display.text += 'x'

    def soma(self):
        if len(self.get_teclado().display.text) > 0:
            if self.get_teclado().display.text[-2] == '‒':
                self.get_teclado().display.text = self.get_teclado().display.text[:-3]
                self.get_teclado().display.text += ' + '
            elif self.get_teclado().display.text[-2] == '+':
                self.get_teclado().display.text = self.get_teclado().display.text[:-3]
                self.get_teclado().display.text += ' ‒ '
            else:
                self.get_teclado().display.text += ' + '
        else:
            self.get_teclado().display.text += ' + '

    def virgula(self):
        if ',' in self.get_teclado().display.text.split('+')[-1]:
            if self.get_teclado().display.text[-1] == ',':
                return
        else:
            self.get_teclado().display.text += ','

    def validate(self):
        exp_a = ''
        exp_b = ''
        exp_c = ''

        exp_a = re.compile('([-]?\d+)(?=[a-zA-Z]\²)')

        if exp_a == '':
            self.get_teclado().display.text = "Inválido"
        else:
            a = (exp_a.match(self.get_teclado().display.text).group())

        exp_b = re.compile('-?\d+(?![a-zA-Z]\^)(?=[a-zA-Z])')
        exp_c = re.compile('-?\d+')

        b = (exp_b.match(self.get_teclado().display.text).group())
        c = (exp_c.match(self.get_teclado().display.text).group())

        self.get_teclado().display.text = "Válido   a = " + a + ", b = " + b + " e c = " + c
