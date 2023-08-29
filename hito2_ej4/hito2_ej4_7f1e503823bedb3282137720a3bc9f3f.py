class CarroDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        for _ in range(cantidad):
            self.productos.append(producto)

    def calcular_descuento(self):
        cantidad_productos = len(self.productos)
        if cantidad_productos >= 3 and cantidad_productos <= 5:
            if set(self.productos) == {1, 2, 3}:
                return 0.2  # Descuento del 20% para los productos 1, 2 y 3
            elif set(self.productos) == {4, 5}:
                return 0.15  # Descuento del 15% para los productos 4 y 5
        return 0

    def calcular_total(self):
        precios = {
            1: 33.77,
            2: 203,
            3: 27.58,
            4: 348.00,
            5: 51.19
        }
        descuento = self.calcular_descuento()
        total = sum([precios[producto] for producto in self.productos])
        total -= total * descuento
        return round(total, 1)


carro = CarroDeCompras()

while True:
    orden = input("Ingrese su orden (agregar, ver, checkout): ")

    if orden == "agregar":
        productos = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto, cantidad = map(int, productos.split(","))
        carro.agregar_producto(producto, cantidad)
        print("Producto(s) agregado(s) al carro.")

    elif orden == "ver":
        print("Productos en el carro:")
        for producto in carro.productos:
            print(producto)

    elif orden == "checkout":
        total = carro.calcular_total()
        print("Total a pagar: USD", total)
        break

    else:
        print("Orden inválida. Intente nuevamente.")
