descuento = 0
descuento1 = 0
descuento2 = 0
carrito = []
productos = [33.77, 203, 27.58, 348.00, 51.19]
nombres = ["Juego Pokemon X para Nintendo 3DS", "Nintendo 3DS XL", "Juego Mario Kart 7 para Nintendo 3DS",
           "PlayStation 4", "FIFA 16, PlayStation 4"]
carrito_valor = 0


def agregar(compra, cantidad, d1, d2):
    if compra == 0 or compra == 1 or compra == 2:
        d1 += 1
    print(d1)
    if compra == 3 or compra == 4:
        d2 += 1
    print(d2)
    carrito.append([])
    unidades_compradas = "x" + str(cantidad)
    carrito[carrito_valor].append(unidades_compradas)
    carrito[carrito_valor].append(nombres[compra])
    carrito[carrito_valor].append(productos[compra] * cantidad)
    print(carrito)
    return d1, d2


def ver_carro():
    return carrito


def checkout(d1, d2):
    d = 0
    precio = 0
    if d1 >= 3:
        d += 0.2
    #print(d)
    if d2 >= 2:
        d += 0.15
    #print(d)
    for n_carrito in range(len(carrito)):
        precio += carrito[n_carrito][2]
    if d != 0:
        precio = precio - (precio * d)
    precio = round(precio, 1)
    #print(precio)
    print(type(precio))
    return print(precio)


print("""
Bienvenido a la tienda!
-Agregue los productos y las cantidades que desee comprar
1: Juego Pokemon X para Nintendo 3DS, USD 33.77
2: Nintendo 3DS XL, USD 203
3: Juego Mario Kart 7 para Nintendo 3DS, USD 27.58
4: PlayStation 4, USD 348.00
5: FIFA 16, PlayStation 4, USD 51.19
""")

#respuesta = input()
#respuesta = respuesta.split("'")
#for i in range(int(len(respuesta) / 2) + 1):
#    respuesta.pop(i)
#for i in range(len(respuesta)):
while True:
    respuesta = input()
    if respuesta == "ver":
        ver_carro()
    elif respuesta == "checkout":
        checkout(descuento1, descuento2)
        break
    elif respuesta == "salir":
        break
    else:
        respuesta_ = respuesta.split(",")
        print(respuesta_)
        producto = int(respuesta_[0]) - 1
        unidades = int(respuesta_[1])
        comprobar = agregar(producto, unidades, descuento1, descuento2)
        descuento1 = comprobar[0]
        descuento2 = comprobar[1]
        carrito_valor += 1     