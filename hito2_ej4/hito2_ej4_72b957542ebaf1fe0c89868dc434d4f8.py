precios = {
    1: 33.77,
    2: 203.00,
    3: 27.58,
    4: 348.00,
    5: 51.19
}

carro = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

def agregar_producto(producto, cantidad):
    producto = int(producto)
    cantidad = int(cantidad)
    carro[producto] += cantidad

def ver_carro():
    for producto, cantidad in carro.items():
        if cantidad > 0:
            print(f"Producto {producto}: Cantidad {cantidad}")

def checkout():
    total = 0.0

    if carro[1] > 0 and carro[2] > 0 and carro[3] > 0:
        total += (precios[1] + precios[2] + precios[3]) * 0.8
    elif carro[4] > 0 and carro[5] > 0:
        total += (precios[4] + precios[5]) * 0.85
    else:
        for producto, cantidad in carro.items():
            total += precios[producto] * cantidad

    print(f"Total a pagar: ${round(total, 1)}")

if __name__ == "__main__":
    while True:
        orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            ver_carro()
        elif orden == "checkout":
            checkout()
            break
        else:
            producto, cantidad = orden.split(",")
            agregar_producto(producto, cantidad)
