# -*- encoding: utf-8 -*-
import os

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout


class SolutionScroll(GridLayout):
    steps = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_text(self, text):
        self.steps.text = text








