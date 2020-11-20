#Carlos alfonso Barrón Rivera
#Jan Mario Gasca Molinero
#Miguel Bañuelos Ramos
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *

from numpy.core.fromnumeric import ptp

ventana = tkinter.Tk()
ventana.title("Graficador de funciones")
ventana.configure(background = 'old lace')
ta = ventana.geometry("1000x700")

plt.style.use('dark_background')


fig = Figure()
grafica = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=ventana)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, ventana)  # barra de iconos
#toolbar.update()
#canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

act_rango = False
ul_ran = ""
ran = ""


def animar(i):
    global act_rango
    global ul_ran
    if act_rango == True:
        try:
            lmin = float(rango[0])
            lmax = float(rango[1])
            if lmin < lmax:
                x = np.arange(lmin, lmax, .01)
                ul_ran = [lmin, lmax]
            else:
                act_rango = False
        except:
            messagebox.showwarning("Error", " Separa por comas los valores, intentalo de nuevo.")
            act_rango = False
            entrada_rango.delete(0, len(entrada_rango.get()))
    else:
        if ul_ran != "":
            x = np.arange(ul_ran[0], ul_ran[1], .01)
        else:
            x = np.arange(0, 5, .01)   #trae valores de x para el rango ide -2 a por default
    try:
        info = eval(info_graficar_f1)#informacion grafica 1
        info2 = eval(info_graficar_f2)#informacion grafica 2
        #grafica.clear()
        grafica.plot(x, info)#graficar f1
        grafica.plot(x, info2)#graficar f2
    except:
        grafica.plot()
    grafica.axhline(0, color="red")#color dl eje x
    grafica.axvline(0, color="red")#color dl eje y
    ani.event_source.stop()  # DETIENE ANIMACIÓN

ani = animation.FuncAnimation(fig, animar, interval=1000)

def representar():
    global info_graficar_f1
    global info_graficar_f2
    global rango
    global act_rango
    funcion_1 = entrada_funcion1.get()
    funcion_2 = entrada_funcion2.get()

    if entrada_rango.get() != "":
        rango = entrada_rango.get().split(",")
        act_rango = True
    funcion_1_procesada = funcion_1.replace("sin", "np.sin").replace("cos", "np.cos").replace("log", "np.log").replace("tan", "np.tan").replace("sqrt", "np.sqrt")
    if funcion_1_procesada.find("ln") != -1:
        funcion_1_procesada = "np.divide("+funcion_1_procesada.replace("ln", "np.log")+",np.log(np.e))"
    info_graficar_f1 = funcion_1_procesada
    ani.event_source.start()  # INICIA/REANUDA ANIMACIÓN

    funcion_2_procesada = funcion_2.replace("sin", "np.sin").replace("cos", "np.cos").replace("log", "np.log").replace("tan", "np.tan").replace("sqrt", "np.sqrt")
    if funcion_2_procesada.find("ln") != -1:
        funcion_2_procesada = "np.divide("+funcion_2_procesada.replace("ln", "np.log")+",np.log(np.e))"
    info_graficar_f2 = funcion_2_procesada
    ani.event_source.start()  # INICIA/REANUDA ANIMACIÓN


plt.show()


etiqueta_rango = tkinter.Label(master=ventana, text="Ingresa el rango de la funcion : ")
etiqueta_f_1 = tkinter.Label(master=ventana, text="Ingresa la funcion numero 1 : ")
entrada_funcion1 = tkinter.Entry(master=ventana, width=15)
etiqueta_f_2 = tkinter.Label(master=ventana, text="Ingresa la funcion numero 2 : ")
entrada_funcion2 = tkinter.Entry(master=ventana, width=15)
entrada_rango = tkinter.Entry(master=ventana, width=10)
button = tkinter.Button(master=ventana, text="Graficar", bg="grey", command=representar,width=20)



#entrada_funcion1.pack(side=tkinter.BOTTOM)
etiqueta_rango.pack(side='left')
entrada_rango.pack(side='left')
etiqueta_f_1.pack(side='left')
entrada_funcion1.pack(side='left')
etiqueta_f_2.pack(side='left')
entrada_funcion2.pack(side='left')
button.pack(side='left')

# ets.insert(0,"RANGO DE X")


# ets.insert(0,"RANGO DE X")

tkinter.mainloop()
