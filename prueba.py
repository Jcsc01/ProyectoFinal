import mysql.connector
from ConectarMsql import Conectar
#dato={
#    'user':'root',
#    'password':'',
#    'database':'proyectopy',
#    'host':'127.0.0.1'
#}
#
#mi_conexion=mysql.connector.connect(** dato)
#mi_cursor=mi_conexion.cursor()

c=Conectar()
c.mi_cursor.execute("SELECT * FROM usuario1")
asd=c.mi_cursor.fetchall()
for i in asd:
    print(i[4])
c.mi_conexion.commit()
c.mi_conexion.close()