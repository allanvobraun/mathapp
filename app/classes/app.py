import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# from app import keyboard, topbar, tela  # precisa

kivy.require('1.11.1')


class MainLayout(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.slaves = self.generate_dict_children(self)
        self.set_children()  # TODO retirar wigets padroes

    # aliciona ao dicionario os "netos" do widget
    def set_children(self):
        for children in self.children:
            if hasattr(children, 'children'):  # se o filho tiver filhos
                self.slaves.update(self.generate_dict_children(children))

    #  comprehention de dicionarios com os widgets filhos
    #  { "nome da classe": objeto}
    @staticmethod
    def generate_dict_children(obj):
        return {child.__class__.__name__: child for child in obj.children}

    def get_child(self, name):
        return self.slaves[name]


class MathApp(App):

    def build(self):
        Builder.load_string(open('app/front/mathapp-front.kv', encoding='utf8').read(), rulesonly=True)

        return MainLayout()
