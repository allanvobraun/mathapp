import kivy
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
        self.passos(1, 6, 8)

    def getCor(self):
        return kivy.utils.get_color_from_hex('#0A5B15')

    def teclado(self, info):
        self.tela.text += info

    def apagar(self):
        if self.tela.text[-1] == " ":
            self.tela.text = self.tela.text[:-3]
        else:
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
            if self.tela.text[-2] == '-':
                self.tela.text = self.tela.text[:-3]
                self.tela.text += ' + '
            elif self.tela.text[-2] == '+':
                self.tela.text = self.tela.text[:-3]
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
        exp_a = ''
        exp_b = ''
        exp_c = ''

        exp_a = re.compile('([-]?\d+)(?=[a-zA-Z]\²)')

        if exp_a == '':
            self.tela.text = "Inválido"
        else:
            a = (exp_a.match(self.tela.text).group())

        exp_b = re.compile('-?\d+(?![a-zA-Z]\^)(?=[a-zA-Z])')
        exp_c = re.compile('-?\d+')

        b = (exp_b.match(self.tela.text).group())
        c = (exp_c.match(self.tela.text).group())

        self.tela.text = "Válido   a = " + a + ", b = " + b + " e c = " + c

    def passos(self,a,b,c):
        delta = b**2 - 4 * a * c
        if delta**(1/2) >= 0:
            x1 = (-b + delta ** (1 / 2)) / (2 * a)
            x2 = (-b - delta ** (1 / 2)) / (2 * a)

        formula_delta = "b² -4·a·c"
        formula_raiz = "x = -b ± √Δ / 2·a"

        delta_p1 = f"Δ = {b}² -4·{a}·{c}"
        delta_p1 = f"Δ = {b**2}+({-4*a*c})"
        delta_result = f"Δ = {delta}"

        x1_p1 = f"x' = -{b} + √{delta} / 2{a}"
        x1_p2 = f"x' = {b*(-1)} + {delta**(1/2)} / {2*a}"
        x1_p3 = f"x' = {b * (-1) + delta ** (1 / 2)} / {2 * a}"
        x1_result = f"x' = {x1}"

        x2_p1 = f"x\" = -{b} - √{delta} / 2{a}"
        x2_p2 = f"x\" = {b * (-1)} - {delta ** (1 / 2)} / {2 * a}"
        x2_p3 = f"x\" = {b * (-1) - delta ** (1 / 2)} / {2 * a}"
        x2_result = f'x\" = {x2}'

        print('Passos para o cálculo do delta(Δ):\n')
        print('Δ = ' + formula_delta + '\n' +
              delta_p1 +'\n' +
              delta_result + '\n')

        print('Passos para a resolução de x:\n')
        print(formula_raiz + '\n\n' +
              x1_p1 + '\n' +
              x1_p2 + '\n' +
              x1_p3 + '\n' +
              x1_result + '\n\n' +

              x2_p1 + '\n' +
              x2_p2 + '\n' +
              x2_p3 + '\n' +
              x2_result + '\n\n')
        resultq = "Solução = {x ∈ ℝ | x\' = " + str(x1) + " e " + "x\" = " + str(x2) + "}"
        print(resultq)