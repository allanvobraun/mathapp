# -*- encoding: utf-8 -*-
import kivy.utils
from kivy.app import App
from app.classes.quadratic import get_variables, grafico
from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout


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

    def validate(self):
        tela = self.get_tela()
        result = get_variables(tela.get_text())
        if result[0] is None:
            tela.change_info('Expressão Inválida')
        else:
            tela.change_info(f"Equação: {result[0]}x² + {result[1]}x + {result[2]} = 0 \nCoeficientes: a = {result[0]}, b = {result[1]}  e  c = {result[2]}")
            tela.show_calculation(result[0], result[1], result[2])

            grafico(result[0], result[1], result[2])
