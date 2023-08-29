class CarroCompras:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def imprimir_productos(self):
        for producto, cantidad in self.productos.items():
            print('Producto {}: {} unidades'.format(producto, cantidad))

    def checkout(self):
        total = 0

        # Calcular el valor de los productos sin descuento
        for producto, cantidad in self.productos.items():
            precio = self.obtener_precio(producto)
            subtotal = precio * cantidad
            total += subtotal

        # Aplicar descuentos según los productos en el carro
        if self.tiene_descuento_conjunto():
            total *= 0.8  # Descuento del 20% si se agregan productos 1, 2 y 3
        elif self.tiene_descuento_individual():
            total *= 0.85  # Descuento del 15% si se agregan productos 4 y 5

        # Imprimir el valor total redondeado a un decimal
        print('Total a pagar: {} USD'.format(round(total, 1)))

    def obtener_precio(self, producto):
        precios = {
            1: 33.77,
            2: 203,
            3: 27.58,
            4: 348.00,
            5: 51.19
        }
        return precios.get(producto, 0)

    def tiene_descuento_conjunto(self):
        productos_conjunto = {1, 2, 3}
        return set(self.productos.keys()).issuperset(productos_conjunto)

    def tiene_descuento_individual(self):
        productos_individuales = {4, 5}
        return set(self.productos.keys()).issuperset(productos_individuales)


carro = CarroCompras()

while True:
    orden = input('Ingrese la orden (producto,cantidad / ver / checkout): ')
    if orden == 'ver':
        carro.imprimir_productos()
    elif orden == 'checkout':
        carro.checkout()
        break
    else:
        try:
            producto, cantidad = map(int, orden.split(','))
            carro.agregar_producto(producto, cantidad)
        except ValueError:
            print('Orden inválida. Intente nuevamente.')
