p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
carrito = {}

precios = {1: 33.77,2: 203.0,3: 27.58,4: 348.0,5: 51.19}

descuentos = {(1, 2, 3): 0.2,(4, 5): 0.15}

def agregar_producto(producto, cantidad):
    carrito[producto] = carrito.get(producto, 0) + cantidad

def calcular_total():
    total = sum(precios[producto] * cantidad for producto, cantidad in carrito.items())

    for descuento_productos, descuento_valor in descuentos.items():
        if all(producto in carrito for producto in descuento_productos):
            descuento = descuento_valor
            total -= total * descuento

    return round(total, 1)

while True:
    orden = input("Ingrese la orden (producto,cantidad / ver / checkout): ")
    if orden == "ver":
        print("Productos en el carrito:")
        for producto, cantidad in carrito.items():
            print(f"Producto {producto}: {cantidad} unidades")
    elif orden == "checkout":
        total = calcular_total()
        print(f"Total a pagar: ${total}")
        break
    else:
        try:
            producto, cantidad = map(int, orden.split(","))
            agregar_producto(producto, cantidad)
            print(f"Se agregaron {cantidad} unidades del producto {producto} al carrito.")
        except ValueError:
            print("Orden inválida. Por favor, ingrese una orden válida.")