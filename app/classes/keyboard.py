# -*- encoding: utf-8 -*-
import kivy
from kivy.app import App
from app.classes.quadratic import validate_exp
from kivy.uix.gridlayout import GridLayout
from app.classes.tela import Tela

kivy.require('1.11.1')


class Keyboard(GridLayout):

    def __init__(self, **kwargs):
        super(Keyboard, self).__init__(**kwargs)
        self.cols = 4
        self.master = App.get_running_app()  # Widget pai de todos

    @staticmethod
    def get_cor():
        return kivy.utils.get_color_from_hex('#0A5B15')


    def get_tela(self):
        return self.master.root.get_screen('calculadora').get_child('Tela')

    def write(self, text):
        tela = self.get_tela()
        tela.append_text(text)

    def delete(self):
        tela = self.get_tela()
        try:
            if tela.get_text() == " ":
                tela.remove(3)
            else:
                tela.remove(1)
        except IndexError:
            return

    def clean(self):
        self.get_tela().set_text('')

    def incognita(self):
        tela = self.get_tela()
        if len(tela.get_text()) > 0:
            if tela.get_text()[-1] != 'x':
                tela.append_text('x')
            else:
                tela.remove(1)
                tela.append_text('x²')
        else:
            tela.append_text('x')


    def plus_minus(self):
        tela = self.get_tela()
        text = tela.get_text()
        if len(text) > 0:
            if text[-2] == '‒':
                tela.remove(3)
                tela.append_text(' + ')
            elif text[-2] == '+':
                tela.remove(3)
                tela.append_text(' ‒ ')
            else:
                tela.append_text(' + ')
        else:
            tela.append_text(' + ')

    def virgula(self):
        tela = self.get_tela()
        text = tela.get_text()
        if ',' in text.split('+')[-1]:
            if text[-1] == ',':
                return
        else:
            tela.append_text(',')

    def validade(self):
        tela = self.get_tela()
        result = validate_exp(tela.get_text())
        if result[0] is None:
            tela.change_info('Expressão invalida!')

