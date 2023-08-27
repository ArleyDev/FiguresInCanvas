from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

ventana = Tk()

sFrame=ttk.Style()
sFrame.configure('estiloFrame.TFrame',background="#714b74")


mainFrame=ttk.Frame(ventana,style='estiloFrame.TFrame', padding='40 80 ')
mainFrame.columnconfigure(0,pad=(100))
mainFrame.grid(column=0,row=0,sticky=(N,W,E,S))


seleccion=IntVar()
seleccion.set(2)
print("imprimiendo seleccion")
print(seleccion.get())
ANCHO_CANVAS=600

colorLineaGlobal="#2f0dec"

ventana.columnconfigure(0,weight=1)
ventana.rowconfigure(0,weight=1)

sFrameColum0=ttk.Style()
sFrameColum0.configure('estiloFrame0.TFrame',background="#714b74",padding='40 80')

frameColumna0=ttk.Frame(mainFrame,style='estiloFrame0.TFrame')
# frameColumna0=ttk.Frame(mainFrame,padding='80 120',style='estiloFrame0.TFrame',relief='sunken')
frameColumna0.grid(column=0,row=0)


frameColumna1=ttk.Frame(mainFrame,padding='20 80',style='estiloFrame0.TFrame')

#modify the padding of the frame making more space on the north
frameColumna1.grid(column=1,row=0,sticky=(N,W,E,S))


manual = ttk.Label(frameColumna1)
manual.grid(column=0, row=1, sticky='we')

def callback():
    # get the color chosen by the user
    result = askcolor(color="#6A9662", title = "Escoge un color")
    # result is now a tuple of two values
    # first value is the color in RGB, second value is the color in HEX
    print(result)
    # set the global variable to the color chosen by the user
    global colorLineaGlobal
    colorLineaGlobal = result[1]  

button = Button(frameColumna1, text="Choose a colour", command=callback)

button.grid(column=0,row=2,sticky='we')

def new_func(canvas, i, space):
    space = int(space)
    ANCHO_CANVAS = 600
    
    canvas.create_line(ANCHO_CANVAS, space * i, ANCHO_CANVAS - (i + 1) * space, ANCHO_CANVAS, fill=colorLineaGlobal)
    canvas.create_line(ANCHO_CANVAS, ANCHO_CANVAS - (i * space), ANCHO_CANVAS - (i + 1) * space, 0, fill=colorLineaGlobal)
    canvas.create_line(0, ANCHO_CANVAS - (i * space), (i + 1) * space, 0, fill=colorLineaGlobal)
    canvas.create_line(0, space * i, (i * space) + space, ANCHO_CANVAS, fill=colorLineaGlobal)


def new_func2(canvas, i, space):
    space = int(space)
    ANCHO_CANVAS = 600
    
    canvas.create_line(ANCHO_CANVAS/2, i * 10, (i + 1) * 10 + ANCHO_CANVAS/2, ANCHO_CANVAS/2,fill=colorLineaGlobal)
    canvas.create_line(ANCHO_CANVAS/2, ANCHO_CANVAS - (i * 10), ANCHO_CANVAS/2 - (i + 1) * 10, ANCHO_CANVAS/2,fill=colorLineaGlobal)
    canvas.create_line(ANCHO_CANVAS/2, ANCHO_CANVAS - (i * 10), ANCHO_CANVAS/2 + (i + 1) * 10, ANCHO_CANVAS/2,fill=colorLineaGlobal)
    canvas.create_line(ANCHO_CANVAS/2, i * 10, ANCHO_CANVAS/2 - (i + 1) * 10, ANCHO_CANVAS/2,fill=colorLineaGlobal)


def seleccionFigura(canvas,space,seleccion):
    if seleccion.get()==1:
        diccionarioRango={10:50,20:40,30:30,40:20,50:10}
        space=diccionarioRango[space]
        rango=ANCHO_CANVAS/space
        rango=int(rango)
        for i in range(rango):
            new_func(canvas, i,space)
    
    elif seleccion.get()==2:
        diccionarioRango={10:50,20:40,30:30,40:20,50:10}
        space=diccionarioRango[space]
        rango=ANCHO_CANVAS/space
        rango=int(rango)
        for i in range(rango):
            new_func2(canvas, i,space)


def clearCanvas(canvas):
    canvas.delete("all")

def SeleccionarColor():
    colorS=askcolor(mainFrame,color="#FFFFFF",title="Seleccionar Color")
    print(colorS)



def update_lbl(val):
   manual['text'] = "Scale at " + val

num=IntVar()


logoImagen=PhotoImage(file=r"C:\Users\Jilmer Moreno\Documents\proyectoPython2022\ProyectoFigurasEnCanvas\figurilla5.png")

# Cargamos la imagen "figurilla2.png" en un widget de imagen
logoImagen2=PhotoImage(file=r"C:\Users\Jilmer Moreno\Documents\proyectoPython2022\ProyectoFigurasEnCanvas\figurilla2.png")

canvas=Canvas(frameColumna1,width=600,height=600,bg='white')
canvas.grid(column=0,row=1,sticky=(N,W,E,S))

def imprimir():
    print("imprimiendo")
    print(seleccion.get())

sRadioboton=ttk.Style()
sRadioboton.configure('estilordBtn.TRadiobutton',font='verdana 16',background='#714b74',foreground='white')


# inserting a label on color white on top of the radio buttons withe text "Select a figure:"

label = ttk.Label(frameColumna0, text="       Select a figure: ", background="#714b74", foreground="white", font=("Helvetica", 16))

label.pady = 500

label.grid(column=0, row=1, sticky='we')

# Creamos un botón de radio que, cuando sea seleccionado, asignará el valor entero 1 a la variable seleccion

radiobtn=ttk.Radiobutton(frameColumna0,image=logoImagen,variable=seleccion,value=1,style='estilordBtn.TRadiobutton',command=lambda:(imprimir()))



# Ubicamos el botón en la columna 0 y la fila 2 del marco
radiobtn.grid(column=0,row=2,sticky=(W,E))

# Creamos un botón de radio que, cuando sea seleccionado, asignará el valor entero 2 a la variable seleccion
radiobtn2=ttk.Radiobutton(frameColumna0,image=logoImagen2,variable=seleccion,value=2,style='estilordBtn.TRadiobutton',command=lambda:(imprimir()))
#print(seleccion.get())
# Ubicamos el botón en la columna 0 y la fila 3 del marco
radiobtn2.grid(column=0,row=3,sticky=(W,E))


def new_func1(clearCanvas, frameColumna1, num, seleccion):
    if seleccion.get()==1:
       # scale = tk.Scale(frameColumna1, orient='horizontal', length=200, from_=10, to=50, tickinterval=10,label=["alto","medio","bajo"], variable=num,showvalue=False, resolution=10, command=lambda value=num.get(): (clearCanvas(canvas), func_for(canvas, int(value))))
        scale = tk.Scale(frameColumna1, orient='horizontal', length=200, from_=10, to=50, tickinterval=10, variable=num,showvalue=False, resolution=10, command=lambda value=num.get(): (clearCanvas(canvas), seleccionFigura(canvas, int(value),seleccion)))
        return scale
    elif seleccion.get()==2:
        scale = tk.Scale(frameColumna1, orient='horizontal', length=200, from_=10, to=50, tickinterval=10, variable=num,showvalue=False, resolution=10, command=lambda value=num.get(): (clearCanvas(canvas), seleccionFigura(canvas, int(value),seleccion)))
        return scale


scale = new_func1(clearCanvas, frameColumna1, num, seleccion)
scale.grid(column=0, row=0, sticky='we')
scale.set(10)



botonSalir=ttk.Button(mainFrame,text="Salir",style='TButton', command=ventana.destroy)
botonSalir.grid(column=3,row=2)


ventana.mainloop()