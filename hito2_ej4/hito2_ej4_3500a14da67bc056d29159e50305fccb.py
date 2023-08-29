productos = {
    1: ["Juego Pokemon X para Nintendo 3DS", 33.77],
    2: ["Nintendo 3DS XL", 203],
    3: ["Juego Mario Kart 7 para Nintendo 3DS", 27.58],
    4: ["PlayStation 4", 348.00],
    5: ["FIFA 16, PlayStation 4", 51.19]
}
carro = {}
def imprimir_carro():
    for producto, cantidad in carro.items():
        nombre = productos[producto][0]
        print("Producto:",nombre, "Cantidad:", cantidad)
def checkout():
    total = 0
    for producto, cantidad in carro.items():
        precio = productos[producto][1]
        total += precio * cantidad
    productos_descuento_1 = set([1, 2, 3])
    productos_descuento_2 = set([4, 5])    
    if productos_descuento_1.issubset(carro.keys()):
        total *= 0.8 
    elif productos_descuento_2.issubset(carro.keys()):
        total *= 0.85  
    print("Total a pagar:", round(total, 1))
while True:
    orden = input("Ingrese una orden (ver, checkout): ")
    if orden == "ver":
        imprimir_carro()
    elif orden == "checkout":
        checkout()
        break
    elif "," in orden:
        producto, cantidad = orden.split(",")
        if producto.isdigit() and cantidad.isdigit():
            producto = int(producto)
            cantidad = int(cantidad)
            if producto in productos:
                carro[producto] = carro.get(producto, 0) + cantidad
            else:
                print("Producto inválido.")
        else:
            print("Entrada inválida. Inténtelo de nuevo.")
    else:
        print("Orden inválida. Inténtelo de nuevo.")