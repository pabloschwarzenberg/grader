productos = {
    1: {'nombre': 'Juego Pokemon X para Nintendo 3DS', 'precio': 33.77},
    2: {'nombre': 'Nintendo 3DS XL', 'precio': 203},
    3: {'nombre': 'Juego Mario Kart 7 para Nintendo 3DS', 'precio': 27.58},
    4: {'nombre': 'PlayStation 4', 'precio': 348.00},
    5: {'nombre': 'FIFA 16, PlayStation 4', 'precio': 51.19}
}

carro = {}

class CarroCompras:
    def agregar_producto(self, producto, cantidad):
        producto = int(producto)
        if producto in productos:
            if producto in carro:
                carro[producto] += cantidad
            else:
                carro[producto] = cantidad
            print("Se agregaron {} unidad(es) del producto {} al carro.".format(cantidad, producto))
        else:
            print("El producto no existe.")

    def ver_productos(self):
        if carro:
            print("Productos en el carro:")
            for producto, cantidad in carro.items():
                nombre = productos[producto]['nombre']
                precio = productos[producto]['precio']
                print("{}x - {} - USD {}".format(cantidad, nombre, precio))
        else:
            print("El carro está vacío.")

    def checkout(self, tipoDespacho, direccion):
        total_productos = 0.0

        for producto, cantidad in carro.items():
            precio = productos[producto]['precio']
            total_productos += precio * cantidad

        descuento = 0.0
        if 1 in carro and 2 in carro and 3 in carro:
            descuento = total_productos * 0.2
        elif 4 in carro and 5 in carro:
            descuento = total_productos * 0.15

        if tipoDespacho == 0:  # Despacho Aéreo Normal
            valor_despacho = total_productos * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            valor_despacho = total_productos * 0.3
        else:
            print("Tipo de despacho inválido.")
            return

        total_pagar = total_productos - descuento + valor_despacho

        if "chile" in direccion.lower():
            total_pagar *= 1.2  # Agregar impuesto del 20%

        print("El total a pagar es: USD {}".format(round(total_pagar, 1)))
        return total_pagar

if __name__ == "__main__":
    carro_compras = CarroCompras()

    orden = ""
    while orden != "checkout":
        orden = input("Ingrese una orden (agregar, ver, checkout): ")

        if orden == "agregar":
            datos = input("Ingrese el producto y la cantidad (producto,cantidad): ")
            producto, cantidad = datos.split(",")
            carro_compras.agregar_producto(producto, int(cantidad))
        elif orden == "ver":
            carro_compras.ver_productos()
        elif orden == "checkout":
            tipo_despacho = int(input("Ingrese el tipo de despacho (0: Despacho Aéreo Normal, 1: Despacho Aéreo Express): "))
            direccion = input("Ingrese la dirección de despacho: ")
            carro_compras.checkout(tipo_despacho, direccion)
        else:
            print("Orden inválida. Intente nuevamente.")


