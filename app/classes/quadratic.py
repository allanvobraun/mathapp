

class Quadratic():

    def passos(self,a,b,c):
        delta = b**2 - 4 * a * c
        if delta**(1/2) >= 0:
            x1 = (-b + delta ** (1 / 2)) / (2 * a)
            x2 = (-b - delta ** (1 / 2)) / (2 * a)

        formula_delta = "b² -4·a·c"
        formula_raiz = "x = -b ± √Δ / 2·a"

        delta_p1 = f"Δ = {b}² -4·{a}·{c}"
        delta_p1 = f"Δ = {b**2}+({-4*a*c})"
        delta_result = f"Δ = {delta}"

        x1_p1 = f"x' = -{b} + √{delta} / 2{a}"
        x1_p2 = f"x' = {b*(-1)} + {delta**(1/2)} / {2*a}"
        x1_p3 = f"x' = {b * (-1) + delta ** (1 / 2)} / {2 * a}"
        x1_result = f"x' = {x1}"

        x2_p1 = f"x\" = -{b} - √{delta} / 2{a}"
        x2_p2 = f"x\" = {b * (-1)} - {delta ** (1 / 2)} / {2 * a}"
        x2_p3 = f"x\" = {b * (-1) - delta ** (1 / 2)} / {2 * a}"
        x2_result = f'x\" = {x2}'

        print('Passos para o cálculo do delta(Δ):\n')
        print('Δ = ' + formula_delta + '\n' +
              delta_p1 +'\n' +
              delta_result + '\n')

        print('Passos para a resolução de x:\n')
        print(formula_raiz + '\n\n' +
              x1_p1 + '\n' +
              x1_p2 + '\n' +
              x1_p3 + '\n' +
              x1_result + '\n\n' +

              x2_p1 + '\n' +
              x2_p2 + '\n' +
              x2_p3 + '\n' +
              x2_result + '\n\n')
        resultq = "Solução = {x ∈ ℝ | x\' = " + str(x1) + " e " + "x\" = " + str(x2) + "}"
        print(resultq)