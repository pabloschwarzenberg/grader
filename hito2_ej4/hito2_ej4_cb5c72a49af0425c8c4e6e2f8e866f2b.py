#carro

def cargar_productos(nombre_archivo):
    f = open(nombre_archivo, "r")
    productos = []
    for linea in f:
        arr = linea.split(",")
        productos.append([int(arr[0]), arr[1], float(arr[2]), int(arr[3])])
    f.close()
    return productos

productos = [
    [1, "Juego Pokemon X para Nintendo 3DS", 33.77],
    [2, "Nintendo 3DS XL", 203],
    [3, "Juego Mario Kart 7 para Nintendo 3DS", 27.58],
    [4, "PlayStation 4", 348],
    [5, "FIFA 16, PlayStation 4", 51.19],
]
carrito = []
agregados = 0
while True:
    print("Que desea hacer?")
    print("agregar: Agregar juguete al carrito")
    print("ver: Ver carrito")
    print("checkout: Autorizar la compra")
    opcion = input()

    if opcion == "agregar":
        for i in range(5):
            print(str(productos[i][0]) + ": " + productos[i][1] + ", USD " + str(productos[i][2]))
        entrada = input("Indique codigo y cantidad (codigo,cantidad): ")
        entrada = entrada.split(",")
        if int(entrada[0]) >= 1 and int(entrada[0]) <= 3:
            total = productos[int(entrada[0]) - 1][2] * int(entrada[1])
            dcto = round(total * 0.2 * 100) / 100
            carrito.append([productos[int(entrada[0]) - 1][1], int(entrada[1]), productos[int(entrada[0]) - 1][2], dcto, total])
            agregados += 1
        elif int(entrada[0]) >= 4 and int(entrada[0]) <= 5:
            total = productos[int(entrada[0]) - 1][2] * int(entrada[1])
            dcto = round(total * 0.15 * 100) / 100
            carrito.append([productos[int(entrada[0]) - 1][1], int(entrada[1]), productos[int(entrada[0]) - 1][2], dcto, total])
            agregados += 1
        else:
            print("Opcion invalida!")
    elif opcion == "ver":
        for i in range(agregados):
            print(carrito[i][0] + " - " + str(carrito[i][1]) + " - " + str(carrito[i][2]) + " - " + str(carrito[i][3]))
    elif opcion == "checkout":
        total = 0
        for i in range(agregados):
            total = total + carrito[i][4]
            print(carrito[i][0] + " - " + str(carrito[i][1]) + " - " + str(carrito[i][2]) + " - " + str(carrito[i][3]) + " - Total: " + str(carrito[i][4]))
        print("Total a pagar: " + str(round(total * 10) / 10))
        break
    else:
        print("Opcion invalida! Intente nuevamente")
      