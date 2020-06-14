# -*- encoding: utf-8 -*-
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window


class Imagens(Screen):
    img = ObjectProperty()

    def __init__(self, **kwargs):
        super(Imagens, self).__init__(**kwargs)
        self.imagemAtual = ''

    def on_enter(self, *args):
        super().on_enter(*args)
        if self.name == 'raiz':
            self.imagemAtual = 'assets/images/raiz.jpeg'

        elif self.name == 'concavidade':
            self.imagemAtual = 'assets/images/concavidade.jpeg'

        elif self.name == 'fisica':
            self.imagemAtual = 'assets/images/fisica.jpeg'

        self.img.source = self.imagemAtual

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    @staticmethod
    def voltar(window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'calculadora'
            return True





