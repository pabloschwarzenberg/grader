productos = {
    1: ["Pokemon X para Nintendo 3DS", 33.77],
    2: ["Nintendo 3DS XL", 203],
    3: ["Mario Kart 7 para Nintendo 3DS", 27.58],
    4: ["PlayStation 4", 348.00],
    5: ["FIFA 16, PlayStation 4", 51.19]
}

carro = {}
descuento_conjunto = 0

def mostrar_menu():
    print("\n>>>>PRODUCTOS<<<<")
    for producto, info in productos.items():
        nombre = info[0]
        precio = info[1]
        print(f"[{producto}] {nombre} - USD {precio:.2f}")

def agregar_al_carrito():
    producto = int(input("\nIngrese el número del producto que desea agregar: "))
    if producto in productos:
        cantidad = int(input("\nIngrese la cantidad: "))
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        print("\n***Producto agregado al carrito***")
    else:
        print("\n***Producto no válido***2")

def ver_carrito():
    print("\n>>>>CARRITO<<<<")
    if len(carro) == 0:
        print("\nEl carrito está vacío.")
    else:
        for producto, cantidad in carro.items():
            nombre = productos[producto][0]
            precio_unitario = productos[producto][1]
            subtotal = precio_unitario * cantidad
            print(f"Producto: {nombre} - Cantidad: {cantidad} - Subtotal: USD {subtotal:.2f}")

def terminar_compra():
    total = 0
    for producto, cantidad in carro.items():
        precio_unitario = productos[producto][1]
        subtotal = precio_unitario * cantidad
        total += subtotal

    if len(carro) >= 3:
        descuento_conjunto = 0.2
    elif 4 in carro and 5 in carro:
        descuento_conjunto = 0.15

    total_descuento = total - (total * descuento_conjunto)

    print(f"\nTotal a pagar con descuento: USD {total_descuento:.1f}")

while True:
    mostrar_menu()
    print("\n")
    print("\t>>>>OPCIONES<<<<")
    print("\t[1] Agregar al carrito")
    print("\t[2] Ver carrito")
    print("\t[3] Terminar compra")
    opcion = int(input("\tIngrese el número de la opción deseada: "))

    if opcion == 1:
        agregar_al_carrito()

    elif opcion == 2:
        ver_carrito()
        
    elif opcion == 3:
        terminar_compra()
        break

    else:
        print("\n***Opción inválida. Intente nuevamente***")
