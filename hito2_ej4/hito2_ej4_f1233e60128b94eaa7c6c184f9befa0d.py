p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
# Definición de los productos y sus precios
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203.0},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.0},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Variables para el carro de compras
carro = {}
subtotal = 0.0

# Función para agregar productos al carro
def agregar_al_carro(producto, cantidad):
    if producto in productos:
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
    else:
        print("El producto ingresado no existe.")

# Función para mostrar los productos en el carro
def ver_carro():
    for producto, cantidad in carro.items():
        nombre = productos[producto]["nombre"]
        precio_unitario = productos[producto]["precio"]
        precio_total = precio_unitario * cantidad
        print(f"Producto: {nombre} (Cantidad: {cantidad}) - Precio total: {precio_total:.1f}")
        global subtotal
        subtotal += precio_total

# Función para realizar el checkout
def checkout():
    descuento = 0.0
    if set([1, 2, 3]).issubset(carro.keys()):
        descuento = subtotal * 0.2
    elif set([4, 5]).issubset(carro.keys()):
        descuento = subtotal * 0.15

    total = subtotal - descuento
    print(f"Subtotal: ${subtotal:.1f}")
    print(f"Descuento: ${descuento:.1f}")
    print(f"Total a pagar: ${total:.1f}")

# Programa principal
if __name__ == "__main__":
    while True:
        orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")
        if orden == "checkout":
            checkout()
            break
        elif orden == "ver":
            ver_carro()
        else:
            try:
                producto, cantidad = map(int, orden.split(","))
                agregar_al_carro(producto, cantidad)
            except:
                print("Orden inválida. Por favor ingrese una orden válida.")
     