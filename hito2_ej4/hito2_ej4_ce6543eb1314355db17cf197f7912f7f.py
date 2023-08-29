# Declaración de listas
# p = [codigo,descripcion,preciounitario,comprado,cantidad,costo]
p1=[1,"Pokemon X",33.77,False,0,0.0]
p2=[2,"Nintendo XL",203,False,0,0.0]
p3=[3,"Mario Kart 7",27.58,False,0,0.0]
p4=[4,"PlayStation 4",348.00,False,0,0.0]
p5=[5,"FIFA 16",51.19,False,0,0.0]

# Pruebas de ejecución:
# Para la compra: ['4,3', '1,1', '3,1', 'checkout'] el valor esperado es 1105.3
# Para la compra: ['3,2','1,2','5,1','checkout'] el valor esperado es 173.9
# Para la compra: ['3,3', '1,1', '4,1', 'checkout'] el valor esperado es 464.5

# Declaración de las funciones
# Calcular los montos de las compras parciales
def agregar_carrito(ped,st):
    if ped[0]=="1": # hay una compra del producto 1
        p1[3] = True # el producto fue comprado
        p1[4] = int(ped[1]) # guardar la cantidad
        p1[5] = p1[4]*p1[2] # calcular el monto de la compra
        st = st + p1[5] # sumar el monto de la compra en el subtotal
    elif ped[0]=="2": # hay una compra del producto 2
        p2[3] = True # el producto fue comprado
        p2[4] = int(ped[1]) # guardar la cantidad
        p2[5] = p2[4]*p2[2] # calcular el monto de la compra
        st = st + p2[5] # sumar el monto de la compra en el subtotal
    elif ped[0]=="3": # hay una compra del producto 3
        p3[3] = True # el producto fue comprado
        p3[4] = int(ped[1]) # guardar la cantidad
        p3[5] = p3[4]*p3[2] # calcular el monto de la compra
        st = st + p3[5] # sumar el monto de la compra en el subtotal
    elif ped[0]=="4": # hay una compra del producto 4
        p4[3] = True # el producto fue comprado
        p4[4] = int(ped[1]) # guardar la cantidad
        p4[5] = p4[4]*p4[2] # calcular el monto de la compra
        st = st + p4[5] # sumar el monto de la compra en el subtotal
    elif ped[0]=="5": # hay una compra del producto 5
        p5[3] = True # el producto fue comprado
        p5[4] = int(ped[1]) # guardar la cantidad
        p5[5] = p5[4]*p5[2] # calcular el monto de la compra
        st = st + p5[5] # sumar el monto de la compra en el subtotal
    return st

def verificar_compra(st):
    t = 0.0
    desc123 = 0.0
    if p1[3] and p2[3] and p3[3]:
        desc123 = st * 0.2
    desc45 = 0.0
    if p4[3] and p5[3]:
        desc45 = st * 0.15
    t = st - (desc123 + desc45)
    return t
# Programa principal
subtotal = 0.0
total = 0.0
c = "X"
while c!='checkout':
    c = input("Ingrese el pedido como producto,cantidad: ")
    if c!='checkout':
        c = c.replace(",","") # elimino la , de la cadena
        pedido = list(c) # crea una lista de valores en función de la cadena
        subtotal = agregar_carrito(pedido,subtotal)
    else:
        total = verificar_compra(subtotal)
        print("Total: ",round(total,1))