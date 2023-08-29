p1='1,Pokemon X,33.77'.split(',')
p2='2,Nintendo XL,203'.split(',')
p3='3,Mario Kart 7,27.58'.split(',')
p4='4,PlayStation 4,348.00'.split(',')
p5='5,FIFA 16,51.19'.split(',')

#descuento 20 % producto 1, 2, 3
#descuento 15% producto 4 y 5

lista_de_validacion = ['c','h']
lista_de_productos = []
lista_de_precios = []

def extraer_dos_numeros(incio, final):
    data = str(x[0]) 
    producto = data[0]
    cantidad = data[2]
    x.pop(0)
    return producto,cantidad

def carro_de_compras(producto):
    if int(producto) == 1:
        carrito_de_compras = p1.copy()
    if int(producto) == 2:
        carrito_de_compras = p2.copy()
    if int(producto) == 3:
        carrito_de_compras = p3.copy()
    if int(producto) == 4:
        carrito_de_compras = p4.copy()
    if int(producto) == 5:
        carrito_de_compras = p5.copy()
    else:
        Exception("Producto no encontrado")
        pass
    return carrito_de_compras

def agregar(pedido):
    lista_de_productos.append(pedido)
    return lista_de_productos


def calculadora_de_precio(cantidad):
    dato = datos_carrito[2]
    precio = float(dato) * int(cantidad)
    return precio

def añadir(valor):
    lista_de_precios.append(valor)
    return lista_de_precios

ingresar = input("aquí: ")
x = eval(ingresar)

while len(x)> 1:
    z = extraer_dos_numeros(0, len(x))
    producto = z[0]
    cantidad = z[1]
    datos_carrito = carro_de_compras(producto)
    precio = calculadora_de_precio(cantidad)
    pedido = datos_carrito[1]
    valor = datos_carrito[2]
    while int(cantidad) != 0:
        agregar(pedido)
        añadir(valor)
        cantidad = int(cantidad) - 1
        
#print(lista_de_productos)
#print(lista_de_precios)



if 'checkout' in x:
    if len(lista_de_precios) == 8:
        resultado_precios = float(lista_de_precios[0]) + float(lista_de_precios[1]) + float(lista_de_precios[2]) + float(lista_de_precios[3]) + float(lista_de_precios[4]) + float(lista_de_precios[5]) + float(lista_de_precios[6]) + float(lista_de_precios[7])
    if len(lista_de_precios) == 7:
        resultado_precios = float(lista_de_precios[0]) + float(lista_de_precios[1]) + float(lista_de_precios[2]) + float(lista_de_precios[3]) + float(lista_de_precios[4]) + float(lista_de_precios[5]) + float(lista_de_precios[6])
    if len(lista_de_precios) == 6:
        resultado_precios = float(lista_de_precios[0]) + float(lista_de_precios[1]) + float(lista_de_precios[2]) + float(lista_de_precios[3]) + float(lista_de_precios[4]) + float(lista_de_precios[5])
    if len(lista_de_precios) == 5:
        resultado_precios = float(lista_de_precios[0]) + float(lista_de_precios[1]) + float(lista_de_precios[2]) + float(lista_de_precios[3]) + float(lista_de_precios[4])
    if len(lista_de_precios) == 4:
        resultado_precios = float(lista_de_precios[0]) + float(lista_de_precios[1]) + float(lista_de_precios[2]) + float(lista_de_precios[3])
    if len(lista_de_precios) == 3:
        resultado_precios = float(lista_de_precios[0]) + float(lista_de_precios[1]) + float(lista_de_precios[2])
    if len(lista_de_precios) == 2:
        resultado_precios = float(lista_de_precios[0]) + float(lista_de_precios[1])
    if len(lista_de_precios) == 1:
        resultado_precios = float(lista_de_precios[0])
    if 'FIFA 16' in lista_de_productos and 'PlayStation 4' in lista_de_productos:
        resultado_precios = (resultado_precios * 85)/100
    if 'Pokemon X' in lista_de_productos and 'Nintendo XL' in lista_de_productos and 'Mario Kart 7' in lista_de_productos:
        resultado_precios = (resultado_precios * 80)/100
    print(round(resultado_precios,1))
      