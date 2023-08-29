# Precios de los productos
precios = {
    1: 33.77,
    2: 203.00,
    3: 27.58,
    4: 348.00,
    5: 51.19
}

# Carro de compras
carro = {}

# Función para agregar productos al carro
def agregar_producto(producto, cantidad):
    producto = int(producto)
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

# Función para mostrar los productos en el carro
def mostrar_productos():
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: Cantidad {cantidad}")

# Función para hacer el checkout y calcular el precio total con descuentos
def checkout():
    total = 0
    descuento = 0

    if 1 in carro and 2 in carro and 3 in carro:
        descuento = 0.2
    elif 4 in carro and 5 in carro:
        descuento = 0.15

    for producto, cantidad in carro.items():
        precio = precios[producto]
        total += precio * cantidad

    total -= total * descuento
    total = round(total, 1)

    print(f"Total a pagar: USD {total}")

# Loop principal del programa
while True:
    orden = input("Ingresa tu orden (producto,cantidad / ver / checkout): ")

    if orden == "ver":
        mostrar_productos()
    elif orden == "checkout":
        checkout()
        break
    else:
        producto, cantidad = orden.split(",")
        agregar_producto(producto, int(cantidad))
