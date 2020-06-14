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
        if self.lenght() == True:
            tela = self.get_tela()
            tela.append_text(text)
        else:
            txt = tela.get_text()
            txt = txt[-1]
            txt += ''

    def delete(self):
        tela = self.get_tela()
        try:
            if tela.get_text()[-1] == " ":
                tela.remove(3)
            else:
                tela.remove(1)
        except IndexError:
            return

    def clean(self):
        self.get_tela().set_text('')

    def incognita(self):
        tela = self.get_tela()

        if self.lenght() == True:
            if len(tela.get_text()) > 0:
                if tela.get_text()[-1] != 'x':
                    tela.append_text('x')
                else:
                    tela.remove(1)
                    tela.append_text('x²')
            else:
                tela.append_text('x')
        else:
            txt = tela.get_text()
            txt = txt[-1]
            txt += ''

    def lenght(self):
        tela = self.get_tela()
        if len(tela.get_text()) > 13:
            txt = tela.get_text()
            txt = txt[:-1]
            return False
        else:
            return True

    def plus_minus(self):
        tela = self.get_tela()
        text = tela.get_text()
        if len(text) > 0:
            if len(text) > 2:
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
        else:
            tela.append_text(' + ')

    def validate_plus_minus(self):
        tela = self.get_tela()

        if 'x²' in tela.get_text() and 'x' in tela.get_text().replace('x²', ''):
            if '+' not in tela.get_text() or '‒' not in tela.get_text():
                return False

            else:
                return True

        else:
            index = tela.get_text().find('x²')
            try:
                if tela.get_text()[index + 2] != '':
                    return False
                else:
                    return True

            except IndexError:
                return True

    def validate(self):
        tela = self.get_tela()

        if 'x²' in tela.get_text().replace('x²', '', 1):
            tela.change_info('Expressão Inválida')
            return

        if 'x' in tela.get_text().replace('x²', '').replace('x', '', 1):
            tela.change_info('Expressão Inválida')
            return

        if self.validate_plus_minus() == False:
            tela.change_info('Expressão Inválida')
            return

        result = get_variables(tela.get_text())

        if result[0] is None:
            tela.change_info('Expressão Inválida')
            return

        else:
            tela.change_info(f"Equação: {result[0]}x² + {result[1]}x + {result[2]} = 0 \n"
                             f"Coeficientes: a = {result[0]}, b = {result[1]}  e  c = {result[2]}")
            tela.show_calculation(result[0], result[1], result[2])
            grafico(result[0], result[1], result[2])
