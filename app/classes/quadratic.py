import js_regex as regex


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
            print("Exp invalida sem o x²")
    else:
        a = match_a.group()

    # b
    if match_b is None:
        if "x" in exp.replace("x²", ""):
            b = "1"
        else:
            b = "0"
            print("exp sem o b")
    else:
        b = match_b.group()

    # c
    if match_c is None:
        c = "0"
        print("exp sem o c")
    else:
        c = match_c.group().replace("+ ", "").replace("‒ ", "")

    return [a, b, c]


def passos(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta ** (1 / 2) >= 0:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)

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

    print('Passos para o cálculo do delta(Δ):\n')
    print('Δ = ' + formula_delta + '\n' +
          delta_p1 + '\n' +
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
