from tkinter import *
from tkinter import ttk,font
import time
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
        imagen1 = PhotoImage(file="MapaMundi.png")
        imagen2 = PhotoImage(file="imagenLabel1.png")
        imagen3 = PhotoImage(file="imagen3.png")
        fondo= Label(self.frame,image=imagen1)
        # creamos las etiquetas y botones para el inicio de sesion
        fuente = font.Font(weight='bold',size=15)
        self.clave = StringVar()
        label2 = ttk.Label(self.frame,image=imagen3,text="Bienvenido a Cajerito",font=fuente,foreground="white",compound=CENTER)
        label = ttk.Label(self.frame,image=imagen2,text="INGRESE SU CLAVE",font=fuente,foreground="white",compound=CENTER)
        self.text = ttk.Entry(self.frame,text=self.clave,font=fuente,show='*',width=6)
        self.ingresar = ttk.Button(self.frame,text="Ingresar",command=self.validar,cursor='hand2')
        # ubicamos en la ventana
        fondo.pack()
        self.frame.pack(fill=BOTH,expand=1)
        label2.place(x=130,y=95)
        label.place(x=138,y=150)
        self.text.place(x=200,y=200)
        self.ingresar.place(x=199,y=250)

        self.text.focus_set()
        self.ventana.mainloop()
    # inicio de sesion (prueba)-cambiar valores interactuando con base de datos
    def validar(self):
        if self.clave.get() == "xd":
            print("acceso permitido")
            self.ventana.destroy()
            a=Menu()
        else:
            print("acceso denegado")
            self.clave.set("")
            self.text.focus_set()

# Ventana menu(despues de ingresar la clave)
class Menu():
    def __init__(self):
        self.ventana2 = Tk()
        self.ventana2.title("Menu")
        self.ventana2.geometry('500x500+450+150')
        self.ventana2.resizable(0,0)
        self.frame2 = Frame(self.ventana2)
        self.frame2.config(bg='#4169E1',relief='ridge',bd=10)

        imagen1 = PhotoImage(file="MapaMundi.png")
        imagen4 = PhotoImage(file="imagen4.png")
        fondo= Label(self.frame2,image=imagen1)
        self.fuente = font.Font(weight='bold',size=15)
        label = ttk.Label(self.frame2,image=imagen4,text="¿Qué operación desea realizar?",font=self.fuente,foreground='white',compound=CENTER)
        self.consulta = ttk.Button(self.frame2,text="Consulta de Datos",command=self.datos,cursor='hand2')
        self.cambio_de_clave = ttk.Button(self.frame2,text="Cambio de Clave",command=self.cambiarClave,cursor='hand2')
        self.cobro_efectivo = ttk.Button(self.frame2,text="Cobro en efectivo",command=self.retirar,cursor='hand2')
        self.trasnferencias = ttk.Button(self.frame2,text="Transferencias",command=self.transferir,cursor='hand2')
        self.salir = ttk.Button(self.frame2,text="Salir",command=self.salir,cursor='hand2')
        
        fondo.pack()
        self.frame2.pack(fill=BOTH,expand=1)
        label.place(x=90,y=90)
        self.consulta.place(x=100,y=150)
        self.cambio_de_clave.place(x=300,y=150)
        self.cobro_efectivo.place(x=100,y=300)
        self.trasnferencias.place(x=300,y=300)
        self.salir.place(x=195,y=400)

        self.ventana2.mainloop()
    # Funciones de botones
    def datos(self):
        self.consulta_de_datos=Toplevel()
        self.consulta_de_datos.geometry('300x200+550+300')
        self.consulta_de_datos.resizable(1,1)
        self.consulta_de_datos.title("Datos del usuario")

        self.boton_volver = ttk.Button(self.consulta_de_datos,text="Volver",command=self.consulta_de_datos.destroy)
        label_nombre = ttk.Label(self.consulta_de_datos,text="USUARIO:",font=self.fuente,foreground='white') 
        label_dni = ttk.Label(self.consulta_de_datos,text="DNI:",font=self.fuente,foreground='white')
        label_saldo = ttk.Label(self.consulta_de_datos,text="SALDO ACTUAL:",font=self.fuente,foreground='white')
        
        label_nombre.pack(side=TOP)
        label_dni.pack(side=TOP)
        label_saldo.pack(side=TOP)
        self.boton_volver.pack(side=TOP)

        self.consulta_de_datos.transient(master=self.ventana2)
        self.consulta_de_datos.grab_set()
        self.ventana2.wait_window(self.consulta_de_datos)
    def cambiarClave(self):
        self.ventana2.destroy()
    def retirar(self):
        self.ventana2.destroy()
    def transferir(self):
        self.ventana2.destroy()
    def salir(self):
        self.ventana2.destroy()
        b=Cajerito()

# Ventana consulta de saldos
#class VentanaConsulta():
#    def __init__(self):
#        self.ventana3 = Tk()
#        self.ventana3.title("Consulta de Saldos")
#        self.ventana3.geometry('500x500+450+150')
#        self.ventana3.resizable(0,0)
#        self.frame3 = Frame(self.ventana3)
#        self.frame3.config(bg='#4169E1',relief='ridge',bd=10)
#
#        imagen1 = PhotoImage(file="MapaMundi.png")
#        fondo= Label(self.frame3,image=imagen1)
#        fuente = font.Font(weight='bold',size=15)
#
#        label_nombre = ttk.Label(self.frame3,text="USUARIO:",font=fuente,foreground='white') 
#        label_dni = ttk.Label(self.frame3,text="DNI:",font=fuente,foreground='white') 
#        label_saldo = ttk.Label(self.frame3,text="SALDO ACTUAL:",font=fuente,foreground='white') 
#
#
#        fondo.pack()
#        self.frame3.pack(fill=BOTH,expand=1)
#        self.ventana3.mainloop()

# prueba de interfaz
b=Cajerito()
