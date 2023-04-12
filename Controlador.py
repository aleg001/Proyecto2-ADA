from ProgramacionDinamica import *
from DivideConquer import *
from AnalisisEmpirico import *

Capacidad = 50
Pesos = [10, 20, 30]
Valores = [60, 100, 120]
Items = 3


def main(arg, arg2):
    try:
        arg = int(arg)
    except:
        print("Error: Argumento no válido")

    try:
        arg2 = int(arg2)
    except:
        print("Error: Argumento no válido")

    if arg == 1:
        print("Programación Dinámica")
        for i in range(arg2):
            result = knapsack_PD(Capacidad, Pesos, Valores, Items)
        print("Resultado del valor máximo a cargar en el Knapsack: ", result)

    if arg == 2:
        print("Divide and Conquer")
        for i in range(arg2):
            result = knapsack_DC(Capacidad, Pesos, Valores, Items)
        print("Resultado del valor máximo a cargar en el Knapsack: ", result)

    if arg == 3:
        print("Análisis Empírico")
        Simulacion()
