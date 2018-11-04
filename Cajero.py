from tkinter import *
from tkinter import ttk,font

class Cajerito():
    def __init__(self):
        # creamos y configuramos la ventana principal
        self.ventana = Tk()
        self.ventana.title("Cajerito.-Ingreso de clave")
        self.ventana.geometry('500x500+450+150')
        self.ventana.resizable(0,0)
        # Creamos un frame y lo metemos dentro de la ventana
        self.frame = Frame(self.ventana)
        self.frame.config(bg='#4169E1',relief='ridge',bd=10)
        # Colocamos una Imagen de fondo
        self.imagen1 = PhotoImage(file="MapaMundi.png")
        self.imagen2 = PhotoImage(file="imagenLabel1.png")
        self.fondo= Label(self.frame,image=self.imagen1)
        # creamos las etiquetas y botones para el inicio de sesion
        fuente = font.Font(weight='bold',size=15)
        self.clave = StringVar()
        self.label = ttk.Label(self.frame,image=self.imagen2,text="INGRESE SU CLAVE",font=fuente,foreground="white",compound=CENTER)
        self.text = ttk.Entry(self.frame,text=self.clave,font=fuente,show='*',width=6)
        self.ingresar = ttk.Button(self.frame,text="Ingresar",command=self.validar,cursor='hand2')
        # ubicamos en la ventana
        self.fondo.pack()
        self.frame.pack(fill=BOTH,expand=1)
        self.label.place(x=138,y=150)
        self.text.place(x=200,y=200)
        self.ingresar.place(x=199,y=250)

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
