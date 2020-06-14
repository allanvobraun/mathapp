# -*- encoding: utf-8 -*-
import kivy.utils
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from app.classes.calculation import Calculation
import app.classes.quadratic as quadratic


class Tela(GridLayout):
    display = ObjectProperty()
    information = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.sview = None
        self.result = None
        self.solution_scroll = None
        self.master = App.get_running_app()  # Widget pai de todos

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

    def get_solution_tela(self):
        return self.master.root.get_screen('calculadora').get_child('SolutionScroll')

    def show_calculation(self, a, b, c):
        txt = self.get_text()
        calc = Calculation(equation=txt, a=float(a), b=float(b), c=float(c))
        delta = calc.calc_delta()
        xs = calc.calc_xs()

        if xs is None:
            self.change_info("A equação não possui solução real")
            return

        self.parent.parent.close_teclado()
        steps = quadratic.passos(a=calc.a, b=calc.b, c=calc.c, delta=delta, x1=xs[0], x2=xs[1])
        self.get_solution_tela().set_text(steps)
