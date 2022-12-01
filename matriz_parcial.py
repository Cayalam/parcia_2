from tkinter import *
from tkinter import messagebox 
import random 


def crear_matriz():
    messagebox.showinfo("crear_matriz 1.0", "Hizo clic en el boton crear matriz...")
    
    # Dimensiones de la matriz
    matriz.get = int(input("No. de filas de la Matriz: "))
    n = matriz
    M = []
    for i in range(M):
        M.append([])
    for j in range(n):
        M[i].append(random.randint(1,9))
    
    for k in range(matriz):
        print()
    for j in range(n):
        print(M[k][j], end= "\t")
    

def buscar():
    messagebox.showinfo("buscar 1.0", "El dato que vas a buscar es...")
    buscar1.get= int(input("¿Que numero deseas buscar?: "))
    for i in range(N):
        if buscar1==N:
            buscar1+=1



    



def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara...")
    ventana_principal.destroy()

# variables globales 


#ventana principal

#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Encontrar Numero Matriz")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="blue")

matriz = StringVar()
n= StringVar()
buscar1=StringVar()


#--------------------
#frame entrada datos
#--------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "sky blue", width = 480 , height = 240)
frame_entrada.place(x = 10, y = 10)





# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text = "Encontrar N.o en  una matriz con dimenciones 3x3")
titulo.config(bg = "sky blue", fg = "black", font = ("ALGERIAN",12))
titulo.place(x = 15, y = 20)
# Etiqueta para el numero que deseas buscar
lb_buscar = Label(frame_entrada,text= "Buscar = ")
lb_buscar.config(bg="sky blue", fg="dark slate gray", font=("Arial Black",20))
lb_buscar.place(x=20, y=115, width=240, height=30)
# Entry para buscar
entry_buscar = Entry(frame_entrada, textvariable=buscar1)
entry_buscar.config(font=("Arial Black",20), justify=LEFT,fg="dark slate gray")
entry_buscar.focus_set()
entry_buscar.place(x=200, y=115, width=115, height=30)  

# Etiqueta para  El numero de la matriz
lb_matriz = Label(frame_entrada, text = "nxn = ")
lb_matriz.config(bg="sky blue", fg="dark slate gray", font=("Arial Black",20))
lb_matriz.place(x=20, y=50, width=240, height=30)


# Entry para x
entry_matriz = Entry(frame_entrada, textvariable=matriz)
entry_matriz.config(font=("Arial Black",20), justify=LEFT,fg="dark slate gray")
entry_matriz.focus_set()
entry_matriz.place(x=200, y=50, width=115, height=30)  

#--------------------
#frame operaciones
#--------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "sky blue", width = 480 , height = 120)
frame_operaciones.place(x = 10, y = 320)


# Boton para Invertir Numero

bt_matriz = Button(frame_entrada, text="crear_matriz",command=crear_matriz)
bt_matriz.place(x=212, y=83, width=100, height=30)





#Boton borrar
bt_buscar= Button(frame_entrada, text="Buscar",command=buscar)
bt_buscar.place(x=212, y=150, width=100, height=30)

# Boton salir
#fotoon= PhotoImage(file="img/descarga.png")
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=335, y=45, width=100, height=30)

# fram resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="sky blue", width=480, height=100)
frame_resultados.place(x=10, y = 390)

#area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="Khaki4", fg="black", font=("Arial Black",16))
t_resultados.place(x=10,y=10, width=460, height= 80)

ventana_principal.mainloop()