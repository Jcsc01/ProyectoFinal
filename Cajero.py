from tkinter import *
from tkinter import ttk,font

class Cajerito():
    def __init__(self):
        # creamos y configuramos la ventana principal
        self.ventana = Tk()
        self.ventana.title("Cajerito.-Ingreso de clave")
        #self.ventana.geometry('500x500+450+150')
        self.ventana.geometry('500x500+450+150')
        self.ventana.resizable(0,0)
        # Creamos un frame y lo metemos dentro de la ventana
        self.frame = Frame(self.ventana)
        self.frame.config(bg='blue')
        
        # creamos las etiquetas y botones para el inicio de sesion
        fuente = font.Font(weight='bold')
        self.clave = StringVar()
        self.label = ttk.Label(self.frame,text="INGRESE SU CLAVE",font=fuente,background='grey')
        self.text = ttk.Entry(self.frame,text=self.clave,show='*',width=6)
        self.ingresar = ttk.Button(self.frame,text="Ingresar",command=self.validar)
        # ubicamos en la ventana
        self.frame.pack(fill=BOTH,expand=1)
        self.label.pack(side=TOP,padx=60,pady=60)
        self.text.pack(side=TOP,padx=20,pady=20)
        self.ingresar.pack(side=TOP,padx=20,pady=20)

        self.text.focus_set()
        self.ventana.mainloop()
    # inicio de sesion (prueba)-cambiar valores interactuando con base de datos
    def validar(self):
        if self.clave.get() == "xd":
            x=ttk.Label(self.frame,text="xd")
            x.pack(side=BOTTOM)
        else:
            print("acceso denegado")
            self.clave.set("")
            self.text.focus_set()
# prueba de interfaz
b=Cajerito()
