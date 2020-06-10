#-*- encoding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
import re

kivy.require('1.11.1')


class Solution(GridLayout):

    def __init__(self, **kwargs):
        super(Solution, self).__init__(**kwargs)

