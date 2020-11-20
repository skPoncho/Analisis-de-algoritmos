import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

def graficadora(ventana_raiz):
    fig = Figure()
    graficadora = fig.add_subplot(111)
    #plt.style.use('dark_background')
    canvas = FigureCanvasTkAgg(fig, master=ventana_raiz)  # CREAR AREA DE DIBUJO DE TKINTER.
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, ventana_raiz)  # barra de iconos
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def iniciar_pantalla():
    ventana_raiz = tkinter.Tk()
    ventana_raiz.title("Graficador de funciones")
    ventana_raiz.configure(background = 'old lace')
    ventana_raiz.geometry("600x600")
    #ventana_raiz.attributes('-fullscreen', True)  

    graficadora(ventana_raiz)

    ventana_raiz.mainloop()

iniciar_pantalla()