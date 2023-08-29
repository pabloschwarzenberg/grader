p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

carro = [] 

def agregar_al_carro(producto_id, cantidad):
    producto_id = int(producto_id)
    cantidad = int(cantidad)

    if producto_id < 1 or producto_id > 5:
        print("Producto no válido.")
        return

    if cantidad <= 0:
        print("Cantidad no válida.")
        return

    producto = None
    if producto_id == 1:
        producto = p1
    elif producto_id == 2:
        producto = p2
    elif producto_id == 3:
        producto = p3
    elif producto_id == 4:
        producto = p4
    elif producto_id == 5:
        producto = p5

    producto_copia = producto.copy()
    producto_copia.append(cantidad)
    carro.append(producto_copia)

    print("Producto agregado al carro.")

def imprimir_carro():
    if len(carro) == 0:
        print("El carro está vacío.")
    else:
        for producto in carro:
            producto_id = producto[0]
            nombre = producto[1]
            precio = producto[2]
            cantidad = producto[3]
            print("Producto {}: {} - Precio: {} - Cantidad: {}".format(producto_id, nombre, precio, cantidad))


# Función para calcular el descuento y el precio total del carro
def calcular_total_con_descuento():
    total = 0.0
    descuento = 0.0

    for producto in carro:
        precio = producto[2]
        cantidad = producto[3]
        total += precio * cantidad

    if len(carro) >= 3 and any(producto[0] in [1, 2, 3] for producto in carro):
        descuento = total * 0.2
    elif len(carro) >= 2 and any(producto[0] in [4, 5] for producto in carro):
        descuento = total * 0.15

    total -= descuento
    total = round(total, 1)

    return total

# Programa principal
while True:
    orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")

    if orden == "ver":
        imprimir_carro()
    elif orden == "checkout":
        total_con_descuento = calcular_total_con_descuento()
        print("Total a pagar con descuento: {}".format(total_con_descuento))
        break
    else:
        try:
            producto_id, cantidad = orden.split(",")
            agregar_al_carro(producto_id, cantidad)
        except ValueError:
            print("Orden no válida. Por favor, ingrese en el formato 'producto,cantidad'.")