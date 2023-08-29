def agregar_al_carro(carro, producto, cantidad):
    if producto == 1:
        carro.append((p1[1], p1[2], cantidad))
    elif producto == 2:
        carro.append((p2[1], p2[2], cantidad))
    elif producto == 3:
        carro.append((p3[1], p3[2], cantidad))
    elif producto == 4:
        carro.append((p4[1], p4[2], cantidad))
    elif producto == 5:
        carro.append((p5[1], p5[2], cantidad))
    else:
        print("El producto seleccionado no existe.")

def ver_carro(carro):
    if not carro:
        print("El carro está vacío.")
    else:
        print("Productos en el carro:")
        total = 0
        for producto in carro:
            nombre = producto[0]
            precio = producto[1]
            cantidad = producto[2]
            subtotal = precio * cantidad
            total += subtotal
            print(f"{nombre} - Precio: {precio} - Cantidad: {cantidad} - Subtotal: {subtotal}")
        print(f"Total a pagar: {total}")

def aplicar_descuento(carro):
    descuento1 = 0.2
    descuento2 = 0.15
    productos_descuento1 = [1, 2, 3]
    productos_descuento2 = [4, 5]
    total = 0
    for producto in carro:
        precio = producto[1]
        cantidad = producto[2]
        subtotal = precio * cantidad
        if producto[0] in productos_descuento1:
            subtotal -= subtotal * descuento1
        elif producto[0] in productos_descuento2:
            subtotal -= subtotal * descuento2
        total += subtotal
    return round(total, 1)

carro = []

while True:
    orden = input("¿Qué deseas hacer? (agregar, ver, checkout, salir): ")

    if orden == "agregar":
        entrada = input("Ingrese el producto y la cantidad en el formato 'producto,cantidad': ")
        producto, cantidad = map(int, entrada.split(","))
        agregar_al_carro(carro, producto, cantidad)
    elif orden == "ver":
        ver_carro(carro)
    elif orden == "checkout":
        total_pagar = aplicar_descuento(carro)
        print(f"Total a pagar con descuento: {total_pagar}")
        break
    elif orden == "salir":
        break
    else:
        print("Orden inválida. Intenta nuevamente.")

