class CarroCompras:
    def __init__(self):
        self.productos = {}
        self.descuentos = {
            frozenset({1, 2, 3}): 0.2,
            frozenset({4, 5}): 0.15
        }

    def agregar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def mostrar_productos(self):
        for producto, cantidad in self.productos.items():
            print(f"Producto {producto}: {cantidad} unidades")

    def checkout(self):
        total = 0
        descuento = 0

        for producto, cantidad in self.productos.items():
            precio = self.calcular_precio(producto)
            total += precio * cantidad

            if producto in self.descuentos:
                descuento += precio * cantidad * self.descuentos[producto]

        total -= descuento
        total = round(total, 1)

        print(f"Total a pagar: USD {total}")

    def calcular_precio(self, producto):
        precios = {
            1: 33.77,
            2: 203,
            3: 27.58,
            4: 348.00,
            5: 51.19
        }

        return precios[producto]


if __name__ == "__main__":
    carro = CarroCompras()

    while True:
        orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            carro.mostrar_productos()
        elif orden == "checkout":
            carro.checkout()
            break
        else:
            try:
                producto, cantidad = map(int, orden.split(","))
                carro.agregar_producto(producto, cantidad)
            except ValueError:
                print("Orden inválida. Intente nuevamente.")
