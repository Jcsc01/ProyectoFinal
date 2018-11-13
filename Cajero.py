from tkinter import *
from tkinter import ttk,font
from tkinter import messagebox
from Usuario import Usuario
from ConectarMsql import Conectar

basedatos="usuario1"
class Cajerito():
    def __init__(self):
        self.id=0
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
        self.ingresar = Button(self.frame,text="Ingresar",command=self.validar,cursor='hand2',height=1,width=10)
        
        # ubicamos en la ventana
        fondo.pack()
        self.frame.pack(fill=BOTH,expand=1)
        label2.place(x=130,y=95)
        label.place(x=138,y=150)
        self.text.place(x=200,y=200)
        self.ingresar.place(x=198,y=250)

        self.text.focus_set()
        self.ventana.mainloop()

    def validar(self):
        c=Conectar()
        c.mi_cursor.execute("SELECT * FROM "+basedatos)
        claves=c.mi_cursor.fetchall()
        encontrado=False
        for i in claves:
            if self.clave.get()==i[5]:
                encontrado=True
                self.id=i[0]
        
        c.cerrar()
        if encontrado==True:
            self.ventana.destroy()
            a=Menu(self.id)

        else:
            messagebox.showerror("Error","Clave incorrecta. por favor intenta de nuevo.")
            self.clave.set("")
            self.text.focus_set()
        

# Ventana menu(despues de ingresar la clave)
class Menu():
    def __init__(self,id):
        self.id=id
        self.ventana2 = Tk()
        self.ventana2.title("Menu")
        self.ventana2.geometry('500x500+450+150')
        self.ventana2.resizable(0,0)
        self.frame2 = Frame(self.ventana2)
        self.frame2.config(bg='#4169E1',relief='ridge',bd=10)

        self.imagen1 = PhotoImage(file="MapaMundi.png")
        imagen4 = PhotoImage(file="imagen4.png")
        fondo= Label(self.frame2,image=self.imagen1)
        self.fuente = font.Font(weight='bold',size=15)
        label = ttk.Label(self.frame2,image=imagen4,text="¿Qué operación desea realizar?",font=self.fuente,foreground='white',compound=CENTER)
        self.consulta = Button(self.frame2,text="Consulta de Datos",command=self.datos,cursor='hand2',height=2,width=15)
        self.cambio_de_clave = Button(self.frame2,text="Cambio de Clave",command=self.cambiarClave,cursor='hand2',height=2,width=15)
        self.cobro_efectivo = Button(self.frame2,text="Cobro en efectivo",command=self.retirar,cursor='hand2',height=2,width=15)
        self.trasnferencias = Button(self.frame2,text="Transferencias",command=self.transferir,cursor='hand2',height=2,width=15)
        self.salir = Button(self.frame2,text="Salir",command=self.salir,cursor='hand2',height=1,width=10)
        
        fondo.pack()
        self.frame2.pack(fill=BOTH,expand=1)
        label.place(x=90,y=90)
        self.consulta.place(x=100,y=170)
        self.cambio_de_clave.place(x=270,y=170)
        self.cobro_efectivo.place(x=100,y=300)
        self.trasnferencias.place(x=270,y=300)
        self.salir.place(x=206,y=400)
        self.ventana2.mainloop()
    # Funciones de botones
    def datos(self):
        self.consulta_de_datos=Toplevel()
        self.consulta_de_datos.geometry('300x200+550+300')
        self.consulta_de_datos.resizable(1,1)
        self.consulta_de_datos.title("Datos del usuario")
        self.consulta_de_datos.config(bg='#6495ED')

        c=Conectar()
        c.mi_cursor.execute("SELECT * FROM "+basedatos+" WHERE id="+str(self.id))
        dato_usuario=c.mi_cursor.fetchall()
        #variables de texto
        usuario="Usuario: "
        cuenta="Numero de cuenta: "
        saldo="Saldo actual: "
        # conectamos con mysql
        usuario+=(dato_usuario[0][1]+" "+dato_usuario[0][2])
        cuenta+=dato_usuario[0][4]
        saldo+=str(dato_usuario[0][3])
        # fuente del label
        fuente1 = font.Font(weight='bold',size=13)
        boton_volver = ttk.Button(self.consulta_de_datos,text="Volver",command=self.consulta_de_datos.destroy,cursor='hand2')
        label_nombre = Label(self.consulta_de_datos,text=usuario,font=fuente1,bg='#6495ED') 
        label_cuenta = Label(self.consulta_de_datos,text=cuenta,font=fuente1,bg='#6495ED')
        label_saldo = Label(self.consulta_de_datos,text=saldo,font=fuente1,bg='#6495ED')
        
        c.cerrar()

        label_nombre.grid(row=0,column=0,sticky=W)
        label_cuenta.grid(row=1,column=0,sticky=W)
        label_saldo.grid(row=2,column=0,sticky=W)
        boton_volver.place(x=110,y=150)

        self.consulta_de_datos.transient(master=self.ventana2)
        self.consulta_de_datos.grab_set()
        self.ventana2.wait_window(self.consulta_de_datos)
    def cambiarClave(self):
        self.cambio_clave=Toplevel()
        self.cambio_clave.geometry('300x200+550+300')
        self.cambio_clave.resizable(1,1)
        self.cambio_clave.title("Cambio de clave")
        self.cambio_clave.config(bg='#6495ED')

        self.v_claveActual=StringVar()
        self.v_claveNueva=StringVar()
        fuente1 = font.Font(weight='bold',size=13)
        label_actual=Label(self.cambio_clave,text="Clave actual",font=fuente1,bg='#6495ED')
        entry_actual=ttk.Entry(self.cambio_clave,text=self.v_claveActual,show="*",width=10)
        label_nueva=Label(self.cambio_clave,text="Clave nueva",font=fuente1,bg='#6495ED')
        entry_nueva=ttk.Entry(self.cambio_clave,text=self.v_claveNueva,show="*",width=10)
        boton_confirmar=ttk.Button(self.cambio_clave,text="Cambiar",command=self.aceptar,cursor='hand2')
        boton_volver=ttk.Button(self.cambio_clave,text="Volver",command=self.cambio_clave.destroy,cursor='hand2')
        
        label_actual.grid(row=0,column=0,padx=40,pady=20,sticky=E)
        entry_actual.grid(row=0,column=1,pady=20)
        label_nueva.grid(row=1,column=0,padx=40,pady=20,sticky=E)
        entry_nueva.grid(row=1,column=1,pady=20)
        boton_confirmar.place(x=70,y=150)
        boton_volver.place(x=160,y=150)

        self.cambio_clave.transient(master=self.ventana2)
        self.cambio_clave.grab_set()
        self.ventana2.wait_window(self.cambio_clave)
    def retirar(self):
        self.retiro=Toplevel()
        self.retiro.geometry('300x200+550+300')
        self.retiro.resizable(1,1)
        self.retiro.title("Cobro en efectivo")
        self.retiro.config(bg='#6495ED')
        
        self.v_monto_retirar=IntVar()
        fuente1 = font.Font(weight='bold',size=13)
        label_monto=Label(self.retiro,text="Monto a retirar:",font=fuente1,bg='#6495ED')
        entry_monto=ttk.Entry(self.retiro,text=self.v_monto_retirar)
        boton_confirmar=ttk.Button(self.retiro,text="Confirmar",command=self.aceptar3,cursor='hand2')
        boton_volver=ttk.Button(self.retiro,text="Volver",command=self.retiro.destroy,cursor='hand2')
        self.v_monto_retirar.set("")
        label_monto.grid(row=0,column=0,padx=10,pady=40)
        entry_monto.grid(row=0,column=1,padx=10,pady=40)
        boton_confirmar.place(x=70,y=150)
        boton_volver.place(x=160,y=150)

        self.retiro.transient(master=self.ventana2)
        self.retiro.grab_set()
        self.ventana2.wait_window(self.retiro)
    def transferir(self):
        self.transferencia=Toplevel()
        self.transferencia.geometry('300x200+550+300')
        self.transferencia.resizable(1,1)
        self.transferencia.title("Transferencia")
        self.transferencia.config(bg='#6495ED')

        self.v_numeroCuenta=StringVar()
        self.v_monto=IntVar()
        fuente1 = font.Font(weight='bold',size=13)
        label_numero_cuenta=Label(self.transferencia,text="Numero de cuenta:",font=fuente1,bg='#6495ED')
        entry_numero_cuenta=ttk.Entry(self.transferencia,text=self.v_numeroCuenta)
        label_monto=Label(self.transferencia,text="Monto:",font=fuente1,bg='#6495ED')
        entry_monto=ttk.Entry(self.transferencia,text=self.v_monto)
        boton_confirmar=ttk.Button(self.transferencia,text="Confirmar",command=self.aceptar2,cursor='hand2')
        boton_volver=ttk.Button(self.transferencia,text="Volver",command=self.transferencia.destroy,cursor='hand2')
        self.v_monto.set("")

        label_numero_cuenta.grid(row=0,column=0,pady=20)
        entry_numero_cuenta.grid(row=0,column=1,pady=20)
        label_monto.grid(row=1,column=0,padx=5,pady=10)
        entry_monto.grid(row=1,column=1,padx=5,pady=10)
        boton_confirmar.place(x=70,y=150)
        boton_volver.place(x=160,y=150)

        self.transferencia.transient(master=self.ventana2)
        self.transferencia.grab_set()
        self.ventana2.wait_window(self.transferencia)
    def salir(self):
        self.ventana2.destroy()
        #self.c.cerrar()
        b=Cajerito()
    def aceptar(self):
        # la nueva clave sea de 6 digitos
        c=Conectar()
        c.mi_cursor.execute("SELECT * FROM "+basedatos+" WHERE id="+str(self.id))
        dato_usuario=c.mi_cursor.fetchall()
        if self.v_claveNueva.get()==dato_usuario[0][5]:
            messagebox.showerror("Error","Clave ya usada")
            self.cambio_clave.deiconify()
        elif self.v_claveActual.get()!=dato_usuario[0][5]:
            messagebox.showerror("Error","Clave actual incorrecta")
            self.cambio_clave.deiconify()
        elif self.v_claveNueva.get().isnumeric()==False:
            messagebox.showerror("Error","La clave solo pueden ser digitos")
            self.cambio_clave.deiconify()
        else:
            acepta=messagebox.askquestion("Confirmar","¿Desea cambiar de clave?")
            if acepta=="yes":
                c.mi_cursor.execute("UPDATE "+basedatos+" SET clave='"+self.v_claveNueva.get()+"' WHERE id="+str(self.id))
                messagebox.showinfo("Cambio de clave","Clave cambiada.")
                c.cerrar()
                self.cambio_clave.destroy()
            else:
                self.cambio_clave.deiconify()
    def aceptar2(self):
        c=Conectar()
        c.mi_cursor.execute("SELECT * FROM "+basedatos+" WHERE id="+str(self.id))
        dato_usuario=c.mi_cursor.fetchall()
        c.mi_cursor.execute("SELECT * FROM "+basedatos)
        personas=c.mi_cursor.fetchall()
        encontrado=False
        for i in personas:
            if self.v_numeroCuenta.get()==i[4]:
                encontrado=True
        if encontrado==False:
            messagebox.showerror("Error","No existe una persona con ese numero de cuenta.")
            self.transferencia.deiconify()
        elif self.v_monto.get()>dato_usuario[0][3]:
            messagebox.showerror("Error","No cuenta con ese monto disponible.")
            self.transferencia.deiconify()
        else:
            acepta=messagebox.askquestion("Confirmar","Usted va a depositar "+str(self.v_monto.get())+"al numero de cuenta: "+self.v_numeroCuenta.get()+"\n"+
            "¿Está seguro?")
            if acepta=="yes":
                c.mi_cursor.execute("SELECT * FROM "+basedatos+" WHERE numerocuenta='"+self.v_numeroCuenta.get()+"'")
                cuentas=c.mi_cursor.fetchall()
                s= self.v_monto.get()+cuentas[0][3]
                c.mi_cursor.execute("UPDATE "+basedatos+" SET saldo="+str(s)+" WHERE numerocuenta='"+self.v_numeroCuenta.get()+"'")
                messagebox.showinfo("Transferencia","Transferencia completada con éxito.")
                c.cerrar()
                self.transferencia.destroy()
            else:
                self.transferencia.deiconify()
    
    def aceptar3(self):
        c=Conectar()
        c.mi_cursor.execute("SELECT * FROM "+basedatos+" WHERE id="+str(self.id))
        dato_usuario=c.mi_cursor.fetchall()
       # if str(self.v_monto_retirar.get()).isdecimal==True:
        #    messagebox.showerror("Error","Solo se admite numeros enteros.")
        if self.v_monto_retirar.get()>dato_usuario[0][3]:
            messagebox.showerror("Error","No cuenta con el saldo suficiente.")
            self.retiro.deiconify()
        else:
            acepta=messagebox.askquestion("Confirmar","¿Desea retirar "+str(self.v_monto_retirar.get())+" soles?")
            if acepta=="yes":
                s=dato_usuario[0][3]-self.v_monto_retirar.get()
                c.mi_cursor.execute("UPDATE "+basedatos+" SET saldo="+str(s)+" WHERE id="+str(self.id))
                messagebox.showinfo("Retiro","Monto retirado.")
                c.cerrar()
                self.retiro.destroy()
            else:
                self.retiro.deiconify()

# prueba de interfaz
b=Cajerito()
