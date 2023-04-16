import numpy as np
import matplotlib.pyplot as plt


class Simulacion:
    def __init__(self):
        with open("tiemposDC.txt", "r") as simFile:
            info = simFile.read()
            info_list = [s for s in info.split("\n") if s]
            tiempos = [float(i) for i in info_list]
            self.Histograma(tiempos, "Divide and Conquer")
            DC = tiempos

        with open("tiemposPD.txt", "r") as simFile:
            info = simFile.read()
            info_list = [s for s in info.split("\n") if s]
            tiempos = [float(i) for i in info_list]
            pd = tiempos
            self.Histograma(tiempos, "Programación Dinámica")
        self.ScatterComparativo(DC, pd)

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
        print("\n", titulo)
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

    def ScatterComparativo(self, listaTiempos1, listaTiempos2):
        fig, ax = plt.subplots()
        """ 
        Revisar gráfico de tipo scatter para mostrar los tiempos de ejecución de ambos.
        
        ax.scatter(listaTiempos1, len(listaTiempos1) * [0], label="Divide and Conquer")
        ax.scatter(
            listaTiempos2, len(listaTiempos2) * [1], label="Programación Dinámica"
        )
        """

        plt.show()
