import time
import numpy as np
import sklearn.linear_model as lm
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt


class Simulacion:
    def __init__(self):
        with open("tiemposDC.txt", "r") as simFile:
            info = simFile.read()
            info_list = [s for s in info.split("\n") if s]
            tiempos = [float(i) for i in info_list]
            self.Histograma(tiempos, "Divide and Conquer")

        with open("tiemposPD.txt", "r") as simFile:
            info = simFile.read()
            info_list = [s for s in info.split("\n") if s]
            tiempos = [float(i) for i in info_list]

            self.Histograma(tiempos, "Programación Dinámica")

    def Histograma(self, listaTiempos, titulo):
        X = listaTiempos
        plt.hist(X, bins=10)
        plt.title(titulo)
        plt.show()
        fig, ax = plt.subplots()
        ax.boxplot(listaTiempos)
        ax.set_title(titulo)
        ax.set_ylabel("Tiempo de ejecucion")
        plt.show()
        print(titulo)
        print("Estadística descriptiva:")
        print("Media:", np.mean(listaTiempos))
        print("Mediana:", np.median(listaTiempos))
        print("Desviación Estándar:", np.std(listaTiempos))
        print(
            "Rango intercuartil:",
            np.percentile(listaTiempos, 75) - np.percentile(listaTiempos, 25),
        )
        fig, ax = plt.subplots()
        ax.violinplot(listaTiempos, showmedians=True)
        ax.set_title(titulo)
        ax.set_ylabel("Tiempo de ejecucion")
        plt.show()
