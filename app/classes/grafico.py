# -*- encoding: utf-8 -*-
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

class Grafico(Screen):

    def __init__(self, **kwargs):
        super(Grafico, self).__init__(**kwargs)

    def on_enter(self, *args):
        pass

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'calculadora'
            return True
