from app.database.dbcalculator import DBCalculator


class Calculation:

    def __init__(self, equation: str = None, x1: str = None, x2: str = None):
        self.__uid = None
        self.equation = equation
        self.x1 = x1
        self.x2 = x2

    # select calculation from database
    def get(self, uid) -> None:
        db = DBCalculator()
        calc = db.get_calc(uid)

        if calc is not None:
            self.__uid = calc[0]
            self.equation = calc[1]
            self.x1 = calc[2]
            self.x2 = calc[3]

        del db

    # salva objeto atual no database
    def save(self):
        db = DBCalculator()
        db.insert_calculation(self.equation, self.x1, self.x2)

    def __str__(self) -> str:  # Tostring do python, printa os atributos
        return str(self.__dict__.items()).replace("dict_items", "Calculation")
