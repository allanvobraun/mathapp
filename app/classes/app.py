import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# from app import keyboard, topbar, tela  # precisa

kivy.require('1.11.1')


class MainLayout(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #  comprehention de dicionarios com os widgets filhos
        #  { "nome da classe": objeto"}
        self.slaves = {child.__class__.__name__: child for child in self.children}

    def get_child(self, name):
        return self.slaves[name]

    pass


class MathApp(App):

    def build(self):
        Builder.load_string(open('app/front/mathapp-front.kv', encoding='utf8').read(), rulesonly=True)

        return MainLayout()
