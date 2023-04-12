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
            self.RegresionPolinomial(tiempos, "Divide and Conquer")

        with open("tiemposPD.txt", "r") as simFile:
            info = simFile.read()
            info_list = [s for s in info.split("\n") if s]
            tiempos = [float(i) for i in info_list]

            self.RegresionPolinomial(tiempos, "Programación Dinámica")

    def RegresionPolinomial(self, listaTiempos, titulo):
        conteoTiempos = len(listaTiempos)
        X = np.array([[i] for i in range(conteoTiempos)])
        y = np.array(listaTiempos)
        Polinomial = PolynomialFeatures(degree=2)
        XPolinomial = Polinomial.fit_transform(X)
        Regresion = lm.LinearRegression()
        Regresion.fit(XPolinomial, y)
        print(titulo)
        print(f"{titulo}  Coeficientes: ", Regresion.coef_)
        print(f"{titulo}  Intercepto: ", Regresion.intercept_)
        print(f"{titulo}  R^2: ", Regresion.score(XPolinomial, y))
        plt.title(titulo)
        plt.scatter(X, y)
        plt.plot(X, Regresion.predict(XPolinomial), color="red")
        plt.show()
        fig, ax = plt.subplots()
        ax.boxplot(X)
        boxplot_dict = ax.boxplot(X)
        for median in boxplot_dict["medians"]:
            y_pos = median.get_ydata()[0]
            plt.text(
                median.get_xdata()[0],
                y_pos,
                f"{y_pos:.2f}",
                ha="center",
                va="bottom",
                fontweight="bold",
            )
        plt.title(titulo)
        plt.show()
