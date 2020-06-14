from app.database.dbcalculator import DBCalculator


class Calculation:

    def __init__(self, equation: str = None,
                 x1: str = None,
                 x2: str = None,
                 a: float = None,
                 b: float = None,
                 c: float = None):

        self.__uid = None
        self.equation = equation
        self.x1 = x1
        self.x2 = x2
        self.a = a
        self.b = b
        self.c = c
        self.delta = None

    def calc_delta(self):
        self.delta = self.b ** 2 - 4 * self.a * self.c
        return self.delta

    def calc_xs(self):
        if self.delta >= 0:
            self.x1 = ((self.b * -1) + self.delta ** (1 / 2)) / (2 * self.a)
            self.x2 = ((self.b * -1) - self.delta ** (1 / 2)) / (2 * self.a)
            return self.x1, self.x2
        else:
            return None

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

    @staticmethod
    def get_all() -> list:  # retorna lsita com varios objetos calcucation
        db = DBCalculator()
        all_calcs = db.get_all()

        result = []

        for line in all_calcs:
            calc = Calculation(equation=line[1], x1=line[2], x2=line[3])
            result.append(calc)
        return result

    # salva objeto atual no database
    def save(self):
        db = DBCalculator()
        db.insert_calculation(self.equation, self.x1, self.x2)

    def __str__(self) -> str:  # Tostring do python, printa os atributos
        return str(self.__dict__.items()).replace("dict_items", "Calculation")
