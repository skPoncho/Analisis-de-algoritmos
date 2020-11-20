#Carlos alfonso Barrón Rivera
#Jan Mario Gasca Molinero
#Miguel Bañuelos Ramos

import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

animacion = None

def animate(i):
    print("Hola")
    if animacion != None:
        animacion.event_source.stop()


def graficadora(ventana_raiz):
	fig = Figure()
	graficadora = fig.add_subplot(111)
    #plt.axes(xlim=(0, 2), ylim=(-2, 2))
	plt.style.use('dark_background')
	canvas = FigureCanvasTkAgg(fig, master=ventana_raiz)  # CREAR AREA DE DIBUJO DE TKINTER.
	canvas.draw()
	canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
	toolbar = NavigationToolbar2Tk(canvas, ventana_raiz)  # barra de iconos
	toolbar.update()
	canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
	
	animacion = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()
	graficadora.axhline(0, color="red")
	graficadora.axvline(0, color="red")
	animacion.event_source.stop()
	return graficadora,animacion


def agregar_componente(ventana_raiz):
    txt_ecuacion = tkinter.Entry(master=ventana_raiz, width=60)

    etiqueta= tkinter.Label(ventana_raiz,text="Escribe el rango separado por coma")
    etiqueta.pack()
    etiqueta2= tkinter.Label(ventana_raiz,text="Escribe función")
   
    txt_ecuacion.config(bg="white", justify="left") #  color y posicion de recuadro de inserción de funcion
    boton = tkinter.Button(master=ventana_raiz, text="Graficar", bg="grey")#, command=representar)

    boton.pack(side=tkinter.BOTTOM)

    txt_ecuacion.pack(side=tkinter.BOTTOM)
    etiqueta2.pack(side=tkinter.BOTTOM)

    txt_rangox = tkinter.Entry(master=ventana_raiz, width=40)
    txt_rangox.config(bg="white")
    txt_rangox.pack(side=tkinter.BOTTOM)


def iniciar_pantalla():
    ventana_raiz = tkinter.Tk()
    ventana_raiz.title("Graficador de funciones")
    ventana_raiz.configure(background = 'old lace')
    ventana_raiz.geometry("600x600")
    #ventana_raiz.attributes('-fullscreen', True)  

    grafica,animacion = graficadora(ventana_raiz)
    agregar_componente(ventana_raiz)
    #t = np.arange(-10, 10, 1)
    #grafica.plot(t, 2 * np.sin(2 * np.pi * t))    
    

    ventana_raiz.mainloop()

iniciar_pantalla()