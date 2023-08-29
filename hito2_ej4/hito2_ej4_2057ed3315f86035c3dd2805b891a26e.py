p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16, PlayStation 4", 51.19]

carro = []

def agregar_producto(producto, cantidad):
    for item in carro:
        if item[0] == producto:
            item[1] += cantidad
            return
    carro.append([producto, cantidad])

def mostrar_carro():
    for item in carro:
        print(f"Producto: {item[0]}, Cantidad: {item[1]}")

def aplicar_descuento():
    total = 0
    descuento = 0

    for item in carro:
        if item[0] in [1, 2, 3]:
            total += item[1] * obtener_precio(item[0])
        else:
            descuento += item[1] * obtener_precio(item[0])

    if total > 0:
        total -= total * 0.2
    if descuento > 0:
        descuento -= descuento * 0.15

    return round(total + descuento, 1)

def obtener_precio(producto):
    if producto == 1:
        return p1[2]
    elif producto == 2:
        return p2[2]
    elif producto == 3:
        return p3[2]
    elif producto == 4:
        return p4[2]
    elif producto == 5:
        return p5[2]
    else:
        return 0

if __name__ == "__main__":
    while True:
        orden = input("Ingrese la orden (agregar, ver, checkout): ")

        if orden == "agregar":
            datos = input("Ingrese el producto y cantidad (producto,cantidad): ")
            producto, cantidad = map(int, datos.split(","))
            agregar_producto(producto, cantidad)
        elif orden == "ver":
            mostrar_carro()
        elif orden == "checkout":
            total = aplicar_descuento()
            print(f"Total a pagar: ${total}")
            break
        else:
            print("Orden inválida. Intente nuevamente.")
