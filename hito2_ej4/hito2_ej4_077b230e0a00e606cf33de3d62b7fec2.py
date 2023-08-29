p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

carro = []
total = 0.0

def agregar_producto(producto, cantidad):
    producto_id = int(producto)
    if producto_id == 1 or producto_id == 2 or producto_id == 3:
        descuento = 0.2
    elif producto_id == 4 or producto_id == 5:
        descuento = 0.15
    else:
        print("Producto inválido.")
        return

    for i in range(cantidad):
        carro.append(producto_id)
        total += descuento * obtener_precio(producto_id)

def obtener_precio(producto_id):
    if producto_id == 1:
        return p1[2]
    elif producto_id == 2:
        return p2[2]
    elif producto_id == 3:
        return p3[2]
    elif producto_id == 4:
        return p4[2]
    elif producto_id == 5:
        return p5[2]

def mostrar_carro():
    print("Productos en el carro:")
    for producto_id in carro:
        if producto_id == 1:
            print(f"{p1[0]} - {p1[1]}")
        elif producto_id == 2:
            print(f"{p2[0]} - {p2[1]}")
        elif producto_id == 3:
            print(f"{p3[0]} - {p3[1]}")
        elif producto_id == 4:
            print(f"{p4[0]} - {p4[1]}")
        elif producto_id == 5:
            print(f"{p5[0]} - {p5[1]}")

def checkout():
    print("Productos en el carro:")
    for producto_id in carro:
        print(f"{producto_id} - {obtener_nombre(producto_id)}")
    print("Total a pagar: $", round(total, 1))

def obtener_nombre(producto_id):
    if producto_id == 1:
        return p1[1]
    elif producto_id == 2:
        return p2[1]
    elif producto_id == 3:
        return p3[1]
    elif producto_id == 4:
        return p4[1]
    elif producto_id == 5:
        return p5[1]

if __name__ == "__main__":
    while True:
        orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")
        if orden == "ver":
            mostrar_carro()
        elif orden == "checkout":
            checkout()
            break
        else:
            producto, cantidad = orden.split(",")
            agregar_producto(producto, int(cantidad))
