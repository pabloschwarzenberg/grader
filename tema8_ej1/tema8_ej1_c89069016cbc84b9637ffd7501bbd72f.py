class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularDescuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.precio * 0.1  # 10% de descuento en cada producto
        return descuentos

    def calcularDespacho(self, tipoDespacho):
        valor_productos = sum(producto.precio for producto in self.productos)
        if tipoDespacho == 0:
            return valor_productos * 0.2  # Despacho Aéreo Normal: 20% del valor de los productos
        elif tipoDespacho == 1:
            return valor_productos * 0.3  # Despacho Aéreo Express: 30% del valor de los productos
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcularDescuentos()
        despacho = self.calcularDespacho(tipoDespacho)
        valor_productos = sum(producto.precio for producto in self.productos)

        if 'chile' in direccion.lower():
            impuesto = valor_productos * 0.2  # 20% de impuesto cuando el despacho es hacia Chile
        else:
            impuesto = 0

        valor_total = valor_productos - descuentos + despacho + impuesto
        return valor_total
