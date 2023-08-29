class Tienda:
    def __init__(self):
        self.carro = CarroCompras()

    def agregar_producto(self, producto):
        self.carro.agregar_producto(producto)

    def checkout(self, tipoDespacho, direccion):
        return self.carro.checkout(tipoDespacho, direccion)


class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.precio * producto.descuento
        return descuentos

    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum(producto.precio for producto in self.productos)
        if tipoDespacho == 0:
            return 0.2 * valor_productos
        elif tipoDespacho == 1:
            return 0.3 * valor_productos
        else:
            return 0

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            return 0.2
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)

        valor_productos = sum(producto.precio for producto in self.productos)
        total = valor_productos - descuentos + despacho
        total += impuesto * total

        return total


class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
