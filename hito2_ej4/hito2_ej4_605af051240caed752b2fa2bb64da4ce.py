def agregar_producto(carro, producto, cantidad):
    carro[producto] = carro.get(producto, 0) + cantidad

def ver_carro(carro):
    if len(carro) == 0:
        print("El carro de compras está vacío.")
    else:
        for producto, cantidad in carro.items():
            print("Producto {}: {}".format(producto, cantidad))

def calcular_total(carro):
    total = 0
    for producto, cantidad in carro.items():
        if producto in ["1", "2", "3"]:
            precio = obtener_precio(producto)
            total += precio * cantidad * 0.8  # Aplica descuento del 20%
        elif producto in ["4", "5"]:
            precio = obtener_precio(producto)
            total += precio * cantidad * 0.85  # Aplica descuento del 15%
        else:
            print("Producto inválido: {}".format(producto))

    return round(total, 1)

def obtener_precio(producto):
    precios = {
        "1": 33.77,
        "2": 203.0,
        "3": 27.58,
        "4": 348.0,
        "5": 51.19
    }
    return precios.get(producto, 0.0)

def ejecutar_programa():
    carro = {}

    while True:
        orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            ver_carro(carro)
        elif orden == "checkout":
            total = calcular_total(carro)
            print("Total a pagar: ${}".format(total))
            break
        else:
            try:
                producto, cantidad = orden.split(",")
                agregar_producto(carro, producto, int(cantidad))
            except ValueError:
                print("Orden inválida. Intente nuevamente.")

ejecutar_programa()
