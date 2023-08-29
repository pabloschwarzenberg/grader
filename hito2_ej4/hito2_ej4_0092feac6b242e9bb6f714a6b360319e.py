p1 = [1, "Juego Pokemon X para Nintendo 3DS", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Juego Mario Kart 7 para Nintendo 3DS", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16, PlayStation 4", 51.19]

carro = {}

def agregar_producto(producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def calcular_total():
    total = 0
    for producto, cantidad in carro.items():
        if producto == 1 and cantidad >= 1 and 2 in carro and 3 in carro:
            total += p1[2] * cantidad * 0.8
        elif producto == 4 and cantidad >= 1 and 5 in carro:
            total += (p4[2] + p5[2]) * cantidad * 0.85
        else:
            total += p[producto-1][2] * cantidad
    return round(total, 1)

if __name__ == "__main__":
    while True:
        accion = input("Ingrese una acción (agregar, ver, checkout): ")

        if accion == "agregar":
            entrada = input("Ingrese el producto y la cantidad (producto,cantidad): ")
            producto, cantidad = map(int, entrada.split(","))
            agregar_producto(producto, cantidad)
            print("Producto agregado al carro.")

        elif accion == "ver":
            print("Productos en el carro:")
            for producto, cantidad in carro.items():
                print(f"{p[producto-1][1]} x{cantidad}")

        elif accion == "checkout":
            total = calcular_total()
            print("Checkout:")
            print(f"Total a pagar: USD {total}")
            break

        else:
            print("Acción inválida. Por favor, ingrese una acción válida.")
