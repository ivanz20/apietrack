from fastapi import FastAPI
import models
from pydantic import BaseModel
from typing import Optional
from starlette.middleware.cors import CORSMiddleware
#python -m uvicorn main:app --reload

app = FastAPI()

origins = [
    "http://127.0.0.1:5500/",
    "http://127.0.0.1:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



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
    

@app.get("/")
def index():
    usuarios = models.GetUsers()
    return usuarios

@app.post("/login")
async def loginPage(data : User):
    user = models.LoginForm(data.user,data.password)
    return user

@app.post("/registrar")
async def RegistroPage(data: User):
    user = models.Registrar(data)
    return user

@app.get("/getproductos")
def productos():
    productos = models.GetProducts()
    return productos

@app.post("/registrarproducto")
async def RegistroProducto(data : Producto):
    producto = models.RegistroProducto(data)
    return producto

@app.post("/registrarventa")
async def RegistroVenta(data : Venta):
    venta = models.RegistroVenta(data)
    return venta
    
    
    
@app.get("/getclientes")
def clients():
    clientes = models.GetClients()
    return clientes

@app.get("/getclientebyid/{idcliente}")
def clientsbyid2(idcliente:int):
    cliente = models.GetClientById(idcliente)
    return cliente

@app.post("/registrarcliente")
async def RegistrarCliente(data : Cliente):
    cliente = models.RegistrarCliente(data)
    return cliente

@app.post("/registrarentrega")
async def RegistrarEntrega(data : Entrega):
    cliente = models.RegistrarEntrega(data)
    return cliente

@app.get("/getventas")
def ventas():
    ventas = models.GetVentas()
    return ventas

@app.get("/getventasbyclientid/{idcliente}")
def ventasbyclienteid(idcliente:int):
    ventasbyid = models.GetVentasByClientId(idcliente)
    return ventasbyid

@app.get("/getproductosbyventa/{idventa}")
def clientebyid(idventa: int):
    cliente = models.GetProductosByIdVenta(idventa)
    return cliente

@app.get("/getentregas")
def entregas():
    entregas = models.GetEntregas()
    return entregas
    