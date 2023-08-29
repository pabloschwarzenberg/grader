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

    def calcular_valor_despacho(self, tipoDespacho):
        valor_productos = sum([producto.precio for producto in self.productos])
        if tipoDespacho == 0:
            return valor_productos * 0.2  # Despacho Aéreo Normal (20%)
        elif tipoDespacho == 1:
            return valor_productos * 0.3  # Despacho Aéreo Express (30%)
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        valor_despacho = self.calcular_valor_despacho(tipoDespacho)
        valor_total = sum([producto.precio for producto in self.productos]) - descuentos + valor_despacho
        
        if "chile" in direccion.lower():
            valor_total *= 1.2  # Agregar 20% de impuesto para despacho a Chile

        return valor_total

