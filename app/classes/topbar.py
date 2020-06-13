# -*- encoding: utf-8 -*-
from kivy.uix.boxlayout import BoxLayout


class TopBar(BoxLayout):

    def __init__(self, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.cols = 4

    def get_image(self):
        return "assets/images/baseline_menu_white_48.png"
