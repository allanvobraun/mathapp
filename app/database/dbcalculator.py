import sqlite3


class DBCalculator:

    def __init__(self):
        try:
            self.db = sqlite3.connect('file:app/database/calculation.db')
        except sqlite3.Error as erro:
            msg = "Database error: {}".format(erro)
            self.db = None
            print(msg)
            del self

        except Exception as erro:
            msg = "Exception in : {}".format(erro)
            print(msg)

    def insert_calculation(self, equation, x1, x2):
        cursor = self.db.cursor()
        params = (equation, x1, x2)
        query = """INSERT INTO main.calculations (equation, x1, x2) VALUES (?, ?, ?)"""
        try:
            cursor.execute(query, params)
            self.db.commit()
            print("Operação efetuada com sucesso")
        except sqlite3.Error as erro:
            msg = "Database error: {}".format(erro)
            print(msg)
            self.db.rollback()

    def get_calc(self, uid):
        cursor = self.db.cursor()
        try:
            cursor.execute("""SELECT * FROM main.calculations WHERE id = ?""", (uid,))
            print("Operação efetuada com sucesso")
        except sqlite3.Error as erro:
            msg = "Database error: {}".format(erro)
            print(msg)

        registro = cursor.fetchone()
        if registro is not None:
            return registro
        else:
            print("Calculo não encontrado")
            return None

    def get_all(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("""SELECT * FROM main.calculations""")
            print("Operação efetuada com sucesso")
        except sqlite3.Error as erro:
            msg = "Database error: {}".format(erro)
            print(msg)

        registro = cursor.fetchall()
        if registro is not None:
            return registro
        else:
            print("Banco vazio")
            return None

    def __del__(self):
        # quando desintacia, encerra a conexao automaticamente
        if self.db is not None:
            self.db.close()
