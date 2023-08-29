class CarroDeCompras:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def imprimir_productos(self):
        for producto, cantidad in self.productos.items():
            print(f"Producto {producto}: Cantidad {cantidad}")

    def checkout(self):
        total = 0
        for producto, cantidad in self.productos.items():
            if producto == "1" or producto == "2" or producto == "3":
                total += cantidad * self.obtener_precio_descuento(producto, 0.2)
            elif producto == "4" or producto == "5":
                total += cantidad * self.obtener_precio_descuento(producto, 0.15)

        return round(total, 1)

    def obtener_precio_descuento(self, producto, descuento):
        precios = {
            "1": 33.77,
            "2": 203,
            "3": 27.58,
            "4": 348.00,
            "5": 51.19
        }

        return precios[producto] * (1 - descuento)


if __name__ == "__main__":
    carro = CarroDeCompras()

    while True:
        orden = input("Ingrese la orden (agregar, ver, checkout): ")

        if orden == "agregar":
            producto, cantidad = input("Ingrese el producto y la cantidad: ").split(",")
            carro.agregar_producto(producto, int(cantidad))
        elif orden == "ver":
            carro.imprimir_productos()
        elif orden == "checkout":
            total = carro.checkout()
            print("Total a pagar:", total)
            break
        else:
            print("Orden inválida. Intente nuevamente.")