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

vantana_raiz = tkinter.Tk()
vantana_raiz.title("Graficador de funciones")
vantana_raiz.configure(background = 'old lace')
ta = vantana_raiz.geometry("1000x700")

plt.style.use('dark_background')


fig = Figure()
ax1 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=vantana_raiz)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, vantana_raiz)  # barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

act_rango = False
ul_ran = ""
ran = ""


def animate(i):
    global act_rango
    global ul_ran
    if act_rango == True:
        try:
            lmin = float(ran[0])
            lmax = float(ran[1])
            if lmin < lmax:
                x = np.arange(lmin, lmax, .01)  # .01
                ul_ran = [lmin, lmax]
            else:
                act_rango = False
        except:
            messagebox.showwarning("Error", " Separa por comas los valores, intentalo de nuevo.")
            act_rango = False
            ets.delete(0, len(ets.get()))
    else:
        if ul_ran != "":
            x = np.arange(ul_ran[0], ul_ran[1], .01)  # .01
        else:
            x = np.arange(0, 10, .01)  # .01
    try:
        solo = eval(graph_data)
        ax1.clear()
        ax1.plot(x, solo)
    except:
        ax1.plot()
    ax1.axhline(0, color="red")
    ax1.axvline(0, color="red")
    ani.event_source.stop()  # DETIENE ANIMACIÓN


def representar():
    global graph_data
    global ran
    global act_rango
    texto_orig = et.get()
    if ets.get() != "":
        rann = ets.get()
        ran = rann.split(",")
        act_rango = True
    ta = texto_orig.replace("sin", "np.sin")
    tb = ta.replace("cos", "np.cos")
    tl = tb.replace("log", "np.log")
    tc = tl.replace("tan", "np.tan")
    tr = tc.replace("sqrt", "np.sqrt")
    graph_data = tr
    ani.event_source.start()  # INICIA/REANUDA ANIMACIÓN


ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()
et = tkinter.Entry(master=vantana_raiz, width=60)
etiqueta= tkinter.Label(vantana_raiz,text="Escribe el rango separado por coma")
etiqueta.pack()
#etiqueta2= tkinter.Label(vantana_raiz,text="Escribe función")
#etiqueta2.pack(padx=10 , side=tkinter.CENTER)
et.config(bg="white", justify="left") #  color y posicion de recuadro de inserción de funcion
boton = tkinter.Button(master=vantana_raiz, text="Graficar", bg="grey", command=representar)
boton.pack(side=tkinter.BOTTOM)
et.pack(side=tkinter.BOTTOM)
ets = tkinter.Entry(master=vantana_raiz, width=40)
ets.config(bg="white")
ets.pack(side=tkinter.BOTTOM)
# ets.insert(0,"RANGO DE X")

tkinter.mainloop()
