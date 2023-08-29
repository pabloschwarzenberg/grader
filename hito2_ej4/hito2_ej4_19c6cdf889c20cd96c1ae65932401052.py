p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos = {
    1: ("Juego Pokemon X para Nintendo 3DS", 33.77),
    2: ("Nintendo 3DS XL", 203),
    3: ("Juego Mario Kart 7 para Nintendo 3DS", 27.58),
    4: ("PlayStation 4", 348.00),
    5: ("FIFA 16, PlayStation 4", 51.19)
}

carro = {}

while True:
    accion = input("Ingrese la acción (agregar, ver, checkout): ")

    if accion == "agregar":
        producto, cantidad = input("Ingrese el producto y la cantidad (producto,cantidad): ").split(",")
        producto = int(producto)
        cantidad = int(cantidad)
        if producto in productos:
            carro[producto] = carro.get(producto, 0) + cantidad
            print("Producto agregado al carro.")
        else:
            print("Producto no válido.")

    elif accion == "ver":
        print("Productos en el carro:")
        for producto, cantidad in carro.items():
            nombre, precio = productos[producto]
            print(f"{cantidad} x {nombre} - USD {precio}")

    elif accion == "checkout":
        total = sum(cantidad * productos[producto][1] for producto, cantidad in carro.items())
        if {1, 2, 3}.issubset(carro.keys()):
            total *= 0.8
        elif {4, 5}.issubset(carro.keys()):
            total *= 0.85
        print("Total a pagar: USD", round(total, 1))
        break

    else:
        print("Acción no válida.")