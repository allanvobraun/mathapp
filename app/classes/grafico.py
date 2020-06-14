# -*- encoding: utf-8 -*-
import os

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window


class Grafico(Screen):
    grafico = ObjectProperty()

    def __init__(self, **kwargs):
        super(Grafico, self).__init__(**kwargs)
        self.path = f"{App.get_running_app().user_data_dir}/grafico.png"


    def on_leave(self, *args):
        print("saiu")
        self.clean_grafico()

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)
        self.grafico.souce = self.path
        self.grafico.reload()

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def clean_grafico(self):
        path = self.path
        if os.path.isfile(path):
            print("SIM")
            os.remove(path)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'calculadora'
            return True
