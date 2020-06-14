import random

import js_regex as regex
import kivy
import matplotlib.pyplot as plt
import numpy as np
import os

def grafico(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)

    eq = f'{a}x² + {b}x + {c}'
    delta = (b**2-4*a*c)
    xv = (-b/(2*a))
    yv = -delta/(4*a)

    X = np.arange(-100, 100)
    f = lambda x: a*x**2 + b*x + c
    Y = [f(x) for x in X]

    plt.scatter(xv, yv)
    plt.plot(X, Y)

    if 'grafico.png' in os.listdir('./assets/graficos/'):
        os.remove('assets/graficos/grafico.png')

    plt.savefig(f'assets/graficos/grafico.png')

    return

def get_variables(exp: str) -> list:
    exp_a = regex.compile('([-]?[0-9]+)(?=x²)')
    exp_b = regex.compile('-?[0-9]+(?!x²)(?=x)')
    exp_c = regex.compile(r'(‒ |\+ )?[0-9]+(?!x)( |$)+')

    match_a = exp_a.search(exp)
    match_b = exp_b.search(exp)
    match_c = exp_c.search(exp)

    a = ""
    b = ""
    c = ""

    # a
    if match_a is None:
        if "x²" in exp:
            a = "1"
        else:
            a = None
            print("Coeficiente a não pode ser nulo")
    else:
        a = match_a.group()

    # b
    if match_b is None:
        if "x" in exp.replace("x²", ""):
            b = "1"
        else:
            b = "0"
    else:
        b = match_b.group()

    # c
    if match_c is None:
        c = "0"

    else:
        c = match_c.group().replace("+ ", "").replace("‒ ", "")

    return [a, b, c]


def passos(a: int = None, b: int = None, c: int = None,
           delta: int = None, x1: int = None, x2: int = None) -> str:
    formula_delta = "b² -4·a·c"
    formula_raiz = "x = -b ± √Δ / 2·a"

    delta_p1 = f"Δ = {b}² -4·{a}·{c}"
    delta_p1 = f"Δ = {b ** 2}+({-4 * a * c})"
    delta_result = f"Δ = {delta}"

    x1_p1 = f"x' = -{b} + √{delta} / 2{a}"
    x1_p2 = f"x' = {b * (-1)} + {delta ** (1 / 2)} / {2 * a}"
    x1_p3 = f"x' = {b * (-1) + delta ** (1 / 2)} / {2 * a}"
    x1_result = f"x' = {x1}"

    x2_p1 = f"x\" = -{b} - √{delta} / 2{a}"
    x2_p2 = f"x\" = {b * (-1)} - {delta ** (1 / 2)} / {2 * a}"
    x2_p3 = f"x\" = {b * (-1) - delta ** (1 / 2)} / {2 * a}"
    x2_result = f'x\" = {x2}'

    delta_txt = f'Passos para o cálculo do delta(Δ):\n' \
                f'Δ = {formula_delta}\n' \
                f'{delta_p1}\n' \
                f'{delta_result}\n'

    x_text = f'Passos para a resolução de x:\n' \
             f'{formula_raiz}\n\n' \
             f'{x1_p1}\n' \
             f'{x1_p2}\n' \
             f'{x1_p3}\n' \
             f'{x1_result}\n\n' \
             f'{x2_p1}\n' \
             f'{x2_p2}\n' \
             f'{x2_p3}\n' \
             f'{x2_result}\n\n'
    resultq = "Solução = {x ∈ ℝ | x\' = " + str(x1) + " e " + "x\" = " + str(x2) + "}"
    return f"{delta_txt}\n{x_text}\n{resultq}"


