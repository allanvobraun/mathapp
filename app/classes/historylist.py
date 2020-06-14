from kivy.uix.recycleview import RecycleView

from app.classes.calculation import Calculation


class HistoryList(RecycleView):
    def __init__(self, **kwargs):
        super(HistoryList, self).__init__(**kwargs)
        # self.data = [{'text': str(x)} for x in range(25)]
        self.get_history()

    def get_history(self):
        calc_list = Calculation().get_all()
        final = []
        for calculo in calc_list:
            dic = {'text': f'Equação: {calculo.equation} | Raizes: x\' = {calculo.x1} x\'\' = {calculo.x2}'}
            final.append(dic)

        self.data = final


