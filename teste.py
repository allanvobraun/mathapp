from numpy import sqrt
from numpy import linspace
from matplotlib import pyplot as plt

# Faz os cálulos e retorna, nessa ordem, x1, x2, xv, yv e Delta
def calculate(a,b,c, delta):
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    xv = -b / (2 * a)
    yv = -delta / (4 * a)

    return x1, x2, xv, yv, delta

# Faz a validação do Delta, e em casos que existem raízes Reais chama a função de cálculo
def quadratic(a, b, c):
    delta = (b ** 2) + ((-4 * a) * c)

    if delta < 0:
        print("\nNão existem raízes Reais.\n")
        return 0

    elif delta == 0:
        print("Existem duas raízes Reais e iguais.\n")
        root = calculate(a,b,c,delta)
        return root

    elif delta > 0:
        print("Existem duas raízes Reais e distintas.\n")
        root = calculate(a, b, c, delta)
        return root

# Realiza o plot do gráfico da função quadrática. Os pontos são as raízes x1 e x2
def plot(a,b,c,x1,x2):
    X = linspace(-100, 100)
    f = [a*x**2+b*x+c for x in X]
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.title("Função quadrática")
    plt.plot(X, f, color="blue", linewidth=2.0, linestyle="-")
    plt.scatter(x1, 0)
    plt.scatter(x2, 0)
    plt.show()

# Programa Main, lida com entradas e saídas e chama as funções principais
def program():
    print("------------------------------------------------------------------------")
    print("Raízes da equação quadrática\n")

    a = int(input("Digite o valor de a:"))
    b = int(input("Digite o valor de b:"))
    c = int(input("Digite o valor de c:"))

    result = quadratic(a,b,c)

    if result != 0:
        print(f"Equação:  | {a}x² + {b}x + {c} = 0")
        print(f"Delta(Δ): | {result[4]}")
        print(f"x1:       | {result[0]}")
        print(f"x2:       | {result[1]}")
        print(f"Xv:       | {result[2]}")
        print(f"Yv:       | {result[3]}\n")
        plot(a, b, c, result[0], result[1])


while True:
    program()
