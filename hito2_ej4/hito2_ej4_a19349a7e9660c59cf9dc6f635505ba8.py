productos = {
    1: ["Pokemon X", 33.77],
    2: ["Nintendo XL", 203],
    3: ["Mario Kart 7", 27.58],
    4: ["PlayStation 4", 348.00],
    5: ["FIFA 16", 51.19]
}

carro = []

# Función para agregar productos al carro
def agregar_producto(producto_id, cantidad):
    producto_id = int(producto_id)
    cantidad = int(cantidad)
    carro.append((producto_id, cantidad))

# Función para calcular el precio total del carro
def calcular_precio_total():
    total = 0
    descuento = 0
    
    for producto_id, cantidad in carro:
        producto = productos[producto_id]
        total += producto[1] * cantidad
    
    # Aplicar descuento del 20% si se agregan los productos 1, 2 y 3 al carro
    if all(producto_id in carro for producto_id in [1, 2, 3]):
        descuento += total * 0.2
    
    # Aplicar descuento del 15% si se agregan los productos 4 y 5 al carro
    if any(producto_id in carro for producto_id in [4, 5]):
        descuento += total * 0.15
    
    return round(total - descuento, 1)

# Bucle principal del programa
while True:
    entrada = input("Ingrese un comando (producto,cantidad / ver / checkout): ")
    comando = entrada.split(",")
    
    if comando[0] == "ver":
        print("Productos en el carro:")
        for producto_id, cantidad in carro:
            producto = productos[producto_id]
            print("- {} x {}".format(producto[0], cantidad))
    elif comando[0] == "checkout":
        precio_total = calcular_precio_total()
        print("Total a pagar: USD {:.2f}".format(precio_total))  # Utilizar formato de dos decimales
        break
    else:
        producto_id, cantidad = comando
        agregar_producto(producto_id, cantidad)
        print("Producto agregado al carro.")
