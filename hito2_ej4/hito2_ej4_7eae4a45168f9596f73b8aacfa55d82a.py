class CarroCompras:
    def __init__(self):
        self.carro = []
        self.descuentos = {
            (1, 2, 3): 0.2,
            (4, 5): 0.15
        }

        self.precios = {
            1: 33.77,
            2: 203.00,
            3: 27.58,
            4: 348.00,
            5: 51.19
        }

    def agregar_producto(self, producto, cantidad):
        self.carro.append((producto, cantidad))

    def ver_productos(self):
        print("Productos en el carro:")
        for producto, cantidad in self.carro:
            nombre = self.precios[producto]
            print("Producto", producto, ":", nombre - cantidad, "unidad(es)")

    def calcular_descuento(self):
        descuento = 0
        for productos, porcentaje in self.descuentos.items():
            if all(producto in [p[0] for p in self.carro] for producto in productos):
                descuento = porcentaje
                break
        return descuento

    def calcular_precio_total(self):
        descuento = self.calcular_descuento()
        total = 0
        for producto, cantidad in self.carro:
            precio = self.precios[producto]
            total += precio * cantidad
        return round(total * (1 - descuento), 1)

    def checkout(self):
        precio_total = self.calcular_precio_total()
        print("Carro de compras:")
        self.ver_productos()
        print("Total a pagar: USD", precio_total)


if __name__ == "__main__":
    carro = CarroCompras()

    while True:
        opcion = input("Ingrese la acción que desea realizar (agregar, ver, checkout): ")

        if opcion == "agregar":
            producto, cantidad = input("Ingrese el producto y la cantidad a agregar (producto,cantidad): ").split(",")
            carro.agregar_producto(int(producto), int(cantidad))
        elif opcion == "ver":
            carro.ver_productos()
        elif opcion == "checkout":
            carro.checkout()
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")