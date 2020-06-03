import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require('1.11.1')


class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 2

        # criacao de widgets
        self.label_principal = Label(text="Batata")
        self.name = TextInput(multiline=False)  # instancia um widget que só pode uma linha
        self.button = Button()

        # adicionando no layout
        self.add_widget(self.label_principal)
        self.add_widget(self.name)
        self.add_widget(self.button)


class MathApp(App):

    def build(self):
        return Grid()


MathApp().run()
