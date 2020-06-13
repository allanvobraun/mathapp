from kivy.uix.widget import Widget


class ParentWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_children(self):
        self.slaves = self.generate_dict_children(self)

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
