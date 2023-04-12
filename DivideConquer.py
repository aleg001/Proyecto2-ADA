import time


def knapsack_DC(Capacidad, Pesos, Valores, Items):
    inicio = time.time()
    if Items == 0 or Capacidad == 0:
        return 0
    item_weight = Pesos[Items - 1]
    item_value = Valores[Items - 1]
    if item_weight > Capacidad:
        return knapsack_DC(Capacidad, Pesos, Valores, Items - 1)
    with_item = item_value + knapsack_DC(
        Capacidad - item_weight, Pesos, Valores, Items - 1
    )
    without_item = knapsack_DC(Capacidad, Pesos, Valores, Items - 1)
    final = time.time()
    delta = final - inicio
    with open("tiemposDC.txt", "a") as f:
        f.write(str(delta) + "\n")
    return max(with_item, without_item)
