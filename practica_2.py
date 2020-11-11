#Carlos Alfonso Barrón Rivera 2019630166 equipo 6
#Jan gasca
#Miguel

from matplotlib import pyplot

def f1(x):
    return 2*x

def f2(x):
    return x**2

def f3(x):
    return x**2+4

x = range(-5, 5)# Valores del eje X que toma el gráfico.

pyplot.plot(x, [f1(i) for i in x])# Graficar ambas funciones.
pyplot.plot(x, [f2(i) for i in x])
pyplot.plot(x, [f3(i) for i in x])

pyplot.axhline(0, color="black")# Establecer el color de los ejes.
pyplot.axvline(0, color="black")

pyplot.xlim(-10, 10)# Limitar los valores de los ejes.
pyplot.ylim(-10, 10)
# Guardar gráfico como imágen PNG.
pyplot.savefig("salida.png")
# Mostrarlo.
pyplot.show()
