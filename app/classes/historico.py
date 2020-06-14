# -*- encoding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window


class Historico(Screen):

    def __init__(self, **kwargs):
        super(Historico, self).__init__(**kwargs)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    @staticmethod
    def voltar(window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'calculadora'
            return True
