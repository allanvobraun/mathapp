import pathlib
from app import app

ROOT = pathlib.Path(__file__).parent.absolute()  # diretorio raiz da aplicação


if __name__ == '__main__':
    app.MathApp().run()
