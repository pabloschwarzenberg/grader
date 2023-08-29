class CarroCompras:
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
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return valor_productos * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return valor_productos * 0.3

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            return 0.2
        return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)

        valor_productos = sum([producto.precio for producto in self.productos])
        total_pagar = valor_productos - descuentos + despacho
        total_pagar += total_pagar * impuesto

        return total_pagar
