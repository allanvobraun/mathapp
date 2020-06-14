from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from app.classes.parentwidget import ParentWidget
from app.classes.solution import SolutionScroll
from app.classes.keyboard import Keyboard


class MainLayout(Screen, ParentWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        super().on_enter()
        self.set_children()

        self.get_child("Tela").change_info('Equação')
        try:
            self.close_scroll()

        except KeyError:
            return

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    @staticmethod
    def voltar(window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def close_teclado(self):
        self.children[0].remove_widget(self.get_child("Keyboard"))
        self.children[0].add_widget(SolutionScroll())

    def close_scroll(self):
        self.children[0].remove_widget(self.get_child("SolutionScroll"))
        self.children[0].add_widget(Keyboard())
