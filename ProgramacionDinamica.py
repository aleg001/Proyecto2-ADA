import time


def knapsack_PD(Capacidad, Pesos, Valores, Items):
    inicio = time.time()
    knapsack_matrix = [
        [0 for peso in range(Capacidad + 1)] for item in range(Items + 1)
    ]
    for item in range(Items + 1):
        for peso in range(Capacidad + 1):
            if item == 0 or peso == 0:
                knapsack_matrix[item][peso] = 0
            elif Pesos[item - 1] <= peso:
                knapsack_matrix[item][peso] = max(
                    Valores[item - 1]
                    + knapsack_matrix[item - 1][peso - Pesos[item - 1]],
                    knapsack_matrix[item - 1][peso],
                )
            else:
                knapsack_matrix[item][peso] = knapsack_matrix[item - 1][peso]
    final = time.time()
    delta = final - inicio
    with open("tiemposPD.txt", "a") as f:
        f.write(str(delta) + "\n")
    return knapsack_matrix[Items][Capacidad]
