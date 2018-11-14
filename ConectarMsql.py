import mysql.connector
#import MySQLdb
#diccionario
class Conectar():
    dato={}
    def __init__(self):
        self.dato={
            'user':'root',
            'password':'',
            'database':'proyectopy',
            'host':'127.0.0.1'
        }
        self.mi_conexion=mysql.connector.connect(**self.dato)
        self.mi_cursor=self.mi_conexion.cursor()
        
        #self.mi_conexion=mysql.connector.connect(** self.dato)
        #self.mi_cursor=self.mi_conexion.cursor()
    
    def cerrar(self):
        self.mi_conexion.commit()
        self.mi_cursor.close()
        self.mi_conexion.close()
