# -*- encoding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from app.classes.quadratic import validate_exp
from kivy.uix.gridlayout import GridLayout
from app.classes.tela import Tela

kivy.require('1.11.1')


class Historico(Screen):

    def __init__(self, **kwargs):
        super(Historico, self).__init__(**kwargs)

    def on_enter(self, *args):
        pass

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'calculadora'
            return True




