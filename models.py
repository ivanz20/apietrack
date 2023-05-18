import mysql.connector
import json
from pydantic import BaseModel
from typing import Optional
from db.database import Database
from sqlalchemy import and_, desc

class User(BaseModel):
    UserId:int
    nombre: str
    apellido : str
    user: str
    password: str
    rol : str

class Producto(BaseModel):
    ProductId: int
    NombreProducto: str
    DescripcionProducto: str
    CantidadProducto: int
    PrecioProducto: float

class Cliente(BaseModel):
    idcliente: int
    nombreclient: str
    direccion: str
    celular: str
    email: str
    codigopostal: int
    corlat: float
    coralt: float

class Venta(BaseModel):
    totalventa: int
    idclienteventa: int
    infoproductos : list
    
class Entrega(BaseModel):
    direccion: str
    cliente: str
    coordenadas : str
    idventa : int

def GetUsers():
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        mycursor.execute("SELECT * FROM Usuario")
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
        
    except Exception as e:
        print(e)
        
def GetProducts():
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        mycursor.execute("SELECT * FROM Producto")
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
        
    except:
        print("Error al conectar a la base de datos")

def GetClients():
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        mycursor.execute("SELECT * FROM Cliente")
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
        
    except:
        print("Error al conectar a la base de datos")
        
def GetClientById(id):
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        mycursor.execute("SELECT * FROM Cliente where idcliente = " + str(id))
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
        
    except:
        print("Error al conectar a la base de datos")
        
def GetVentasByClientId(id):
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        mycursor.execute("SELECT * FROM Venta where idclienteventa = " + str(id))
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data, indent=4, sort_keys=True, default=str)
        
    except Exception as e:

        print(e)
        
def GetEntregas():
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        mycursor.execute("SELECT * FROM Entrega")
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data,indent=4, sort_keys=True, default=str)
        
    except Exception as e:
        print(e)

def GetVentas():
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        mycursor.execute("SELECT Venta.idventa, Venta.fechacompra, Venta.totalventa,Cliente.nombrecliente FROM Venta INNER JOIN Cliente ON Venta.idclienteventa=Cliente.idcliente;")
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        print(json_data)
        return json.dumps(json_data,indent=4, sort_keys=True, default=str)
        
    except Exception as e:
        print(e)
        
def LoginForm(user, password):
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        query = "SELECT * FROM Usuario where Usuario = '" + user + "' AND Contra = '" + password + "';"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
        
    except:
        print("Error al conectar a la base de datos")

def GetProductosByIdVenta(id):
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        query = "SELECT Producto.nombreproducto, Producto.precio, listaVenta.cantidadproducto FROM listaVenta INNER JOIN Producto ON listaVenta.idproducto=Producto.idproducto where listaVenta.idventa = " + str(id) + ";"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
        
    except Exception as ex:
        print(ex)
        
def Registrar(data: User):
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        query = "insert into Usuario (Nombre, Apellido, Usuario, Contra, rol) Values ('" + data.nombre + "','" + data.apellido + "','" + data.user + "','" + data.password +"','" + data.rol + "');"
        print(query)
        mycursor.execute(query)
        cnx.commit()
        
        mycursor.execute("select * from Usuario")
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
        
    except Exception as e:
        print(e)
        
def RegistroProducto(data: Producto):
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        query = "insert into Producto  (nombreproducto, descripcionproducto,cantidad, precio) Values ('" + data.NombreProducto + "','" + data.DescripcionProducto + "','" + str(data.CantidadProducto) + "','" + str(data.PrecioProducto) + "');"
        print(query)
        mycursor.execute(query)
        cnx.commit()
        
        mycursor.execute("select * from Producto")
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
        
    except Exception as e:
        print(e)
        
def RegistrarCliente(data: Cliente):
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        query = "insert into Cliente (nombrecliente, direccion, celular,email,codigopostal,cord_lat,cord_alt) Values ('" + data.nombreclient + "','" + data.direccion + "','" + data.celular +"','" + data.email + "'," +  str(data.codigopostal) +"," + str(data.corlat) + "," + str(data.coralt) + ");"
        print(query)
        mycursor.execute(query)
        cnx.commit()
        
        mycursor.execute("select * from Cliente")
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
        
    except Exception as e:
        print(e)

def RegistroVenta(data: Venta):
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        
        query = "insert into Venta  (fechacompra, totalventa,idclienteventa) Values (NOW()," + str(data.totalventa) + "," + str(data.idclienteventa) + ");"
        mycursor.execute(query)
        cnx.commit()
        
        mycursor.execute("SELECT * FROM Venta ORDER BY idventa DESC LIMIT 1")
        myresult = mycursor.fetchall()
        infoRecord = myresult[0]
        idventa = infoRecord[0]
        infoProductos = data.infoproductos
        for n in infoProductos:
            infopro = str(n).split(",")
               
            query = "insert into listaVenta  (cantidadproducto, idproducto,idventa) Values (" + str(infopro[0]) +"," + str(infopro[1]) + "," + str(idventa) + ");"
            mycursor.execute(query)
            cnx.commit()
        
        return json.dumps({"message":"ok"})
        
    except Exception as e:
        print(e)
        
def RegistrarEntrega(data: Entrega):
    try:
        cnx =mysql.connector.connect(user="ivanzv", password="ivanzv",host="slackdroid.cloud",database="ingsoftware")
        print("Conectado a la base de datos")
        mycursor = cnx.cursor()
        query = "insert into Entrega (direccion, cliente, entregado,coordenadas,fechaentrega,idventa) Values ('" + data.direccion + "','" + data.cliente + "',false,'" + data.coordenadas + "',NOW()," + str(data.idventa) +");"
        print(query)
        mycursor.execute(query)
        cnx.commit()
        
        mycursor.execute("select * from Entrega")
        myresult = mycursor.fetchall()
        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data,indent=4, sort_keys=True, default=str)
        
    except Exception as e:
        print(e)
        
GetUsers()