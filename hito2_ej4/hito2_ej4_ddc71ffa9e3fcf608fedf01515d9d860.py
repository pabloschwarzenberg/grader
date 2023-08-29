p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

productos = {1: p1, 2: p2, 3: p3, 4: p4, 5: p5}
carro = {}

while True:
    comando = input("Ingresa un comando (producto,cantidad / ver / checkout): ")

    if comando == "ver":
        print("Contenido del carro:")
        for producto, cantidad in carro.items():
            producto_info = productos.get(producto)
            if producto_info:
                producto_nombre = producto_info[1]
                producto_precio = producto_info[2]
                print("Producto {}: {} - Cantidad {} - Precio: ${}".format(producto, producto_nombre, cantidad, producto_precio))

    elif comando == "checkout":
        total_precio = 0
        descuento = 0

        if {1, 2, 3}.issubset(carro.keys()):
            descuento = 0.2
        elif {4, 5}.issubset(carro.keys()):
            descuento = 0.15

        for producto, cantidad in carro.items():
            producto_info = productos.get(producto)
            if producto_info:
                producto_precio = producto_info[2]
                total_precio += cantidad * producto_precio

        total_precio -= total_precio * descuento
        total_precio = round(total_precio, 1)
        print("Precio total: ${}".format(total_precio))
        break

    else:
        try:
            producto, cantidad = map(int, comando.split(","))
            if 1 <= producto <= 5 and cantidad >= 1:
                if producto in carro:
                    carro[producto] += cantidad
                else:
                    carro[producto] = cantidad
            else:
                print("Producto o cantidad invalida.")
        except:
            print("Comando Invalido.")