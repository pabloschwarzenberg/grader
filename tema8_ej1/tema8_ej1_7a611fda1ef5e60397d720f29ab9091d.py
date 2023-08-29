class CarroDeCompras:
    def __init__(self):
        self.productos = []

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
            return 0.2 * valor_productos  # Despacho Aéreo Normal
        elif tipoDespacho == 1:
            return 0.3 * valor_productos  # Despacho Aéreo Express

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        valor_productos = sum([producto.precio for producto in self.productos])
        total = valor_productos - descuentos + despacho

        if "chile" in direccion.lower():
            total += total * 0.2  # Agregar 20% de impuestos

        return total
