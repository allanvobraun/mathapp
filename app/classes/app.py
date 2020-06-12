import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from app.classes.parentwidget import ParentWidget

# from app import keyboard, topbar, tela  # precisa

kivy.require('1.11.1')


class ScreenControler(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainLayout(Screen, ParentWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        super().on_enter()
        self.__init__()


class MathApp(App):

    def build(self):
        Builder.load_string(open('app/front/mathapp-front.kv', encoding='utf8').read(), rulesonly=True)

        return ScreenControler()
