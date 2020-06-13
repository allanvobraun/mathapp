import pathlib

from kivy import Config

from app.classes import app

ROOT = pathlib.Path(__file__).parent.absolute()  # diretorio raiz da aplicação

if __name__ == '__main__':
    Config.set('graphics', 'width', '375')
    Config.set('graphics', 'height', '667')
    app.MathApp().run()
