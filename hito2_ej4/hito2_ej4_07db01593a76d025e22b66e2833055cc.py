class CarroDeCompras:
    def __init__(self):
        self.carro = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.carro:
            self.carro[producto] += cantidad
        else:
            self.carro[producto] = cantidad

    def mostrar_productos(self):
        for producto, cantidad in self.carro.items():
            print(f"Producto {producto}: {cantidad} unidades")

    def checkout(self):
        total = 0

        for producto, cantidad in self.carro.items():
            if producto in [1, 2, 3] and cantidad >= 1:
                total += cantidad * self.precio_descuento(producto, 0.2)
            elif producto in [4, 5] and cantidad >= 1:
                total += cantidad * self.precio_descuento(producto, 0.15)

        total = round(total, 1)
        print(f"Total a pagar: USD {total}")

    def precio_descuento(self, producto, descuento):
        precios = {
            1: 33.77,
            2: 203.0,
            3: 27.58,
            4: 348.0,
            5: 51.19
        }
        return precios[producto] * (1 - descuento)


carro = CarroDeCompras()

while True:
    orden = input("Ingrese la orden (agregar, ver, checkout): ")

    if orden == "agregar":
        producto, cantidad = map(int, input("Ingrese el producto y la cantidad: ").split(","))
        carro.agregar_producto(producto, cantidad)
    elif orden == "ver":
        carro.mostrar_productos()
    elif orden == "checkout":
        carro.checkout()
        break
    else:
        print("Orden no válida. Intente nuevamente.")
