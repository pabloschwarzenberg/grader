# Definir variables de productos
p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

# Variables para almacenar los productos en el carro
carro = []
subtotal = 0.0

# Función para aplicar descuentos
def aplicar_descuentos(subtotal):
    if set([1, 2, 3]).issubset(carro):
        subtotal *= 0.8  # Descuento del 20% si los productos 1, 2 y 3 están en el carro
    elif set([4, 5]).issubset(carro):
        subtotal *= 0.85  # Descuento del 15% si los productos 4 y 5 están en el carro
    return subtotal

# Función para agregar productos al carro
def agregar_al_carro(producto, cantidad):
    global subtotal
    subtotal += producto[2] * cantidad
    carro.extend([producto[0]] * cantidad)

# Función para mostrar los productos en el carro
def ver_carro():
    print("Productos en el carro:")
    for item in carro:
        producto = None
        if item == 1:
            producto = p1
        elif item == 2:
            producto = p2
        elif item == 3:
            producto = p3
        elif item == 4:
            producto = p4
        elif item == 5:
            producto = p5

        if producto:
            print("- {producto[1]}")

# Función para hacer el checkout
def checkout():
    total = aplicar_descuentos(subtotal)
    print("Total a pagar: USD {round(total, 1)}")

# Ciclo principal del programa
while True:
    accion = input("¿Qué acción deseas realizar? (agregar, ver, checkout, salir): ")

    if accion == "agregar":
        entrada = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto, cantidad = map(int, entrada.split(","))
        if producto == 1:
            agregar_al_carro(p1, cantidad)
        elif producto == 2:
            agregar_al_carro(p2, cantidad)
        elif producto == 3:
            agregar_al_carro(p3, cantidad)
        elif producto == 4:
            agregar_al_carro(p4, cantidad)
        elif producto == 5:
            agregar_al_carro(p5, cantidad)
        else:
            print("Producto no válido.")

    elif accion == "ver":
        ver_carro()

    elif accion == "checkout":
        checkout()
        break

    elif accion == "salir":
        break

    else:
        print("Acción no válida. Inténtalo de nuevo.")
