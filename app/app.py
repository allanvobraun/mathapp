import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from app import keyboard, topbar  # precisa


kivy.require('1.11.1')


class TopBar(BoxLayout):

    def __init__(self, **kwargs):
        super(TopBar, self).__init__(**kwargs)
        self.cols = 4

    def get_image(self):
        return "/home/allanbraun/PycharmProjects/mathapp/assets/images/baseline_menu_white_48.png"


class MainLayout(GridLayout):
    pass


class MathApp(App):

    def build(self):
        Builder.load_string(open('app/mathapp-front.kv', encoding='utf8').read(), rulesonly=True)

        return MainLayout()


