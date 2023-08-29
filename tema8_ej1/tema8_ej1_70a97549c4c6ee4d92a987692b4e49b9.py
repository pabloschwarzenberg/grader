class CarroDeCompras:
    def __init__(self, tienda):
        self.productos = []
        self.tienda = tienda

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.descuento
        return descuentos

    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum([producto.precio for producto in self.productos])
        if tipoDespacho == 0:
            return valor_productos * 0.2  # Despacho Aéreo Normal (20% del valor de los productos)
        elif tipoDespacho == 1:
            return valor_productos * 0.3  # Despacho Aéreo Express (30% del valor de los productos)
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        valor_total = sum([producto.precio for producto in self.productos]) - descuentos + despacho

        if 'chile' in direccion.lower():
            valor_total += valor_total * 0.2  # Agregar 20% de impuesto si el despacho es hacia Chile

        return valor_total
