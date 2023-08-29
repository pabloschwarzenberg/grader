class CarroDeCompras:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def quitar_item(self, item):
        self.items.remove(item)

    def calcular_descuentos(self):
        descuento_total = 0
        for item in self.items:
            descuento = 0.1 * item.cantidad * item.producto.precio
            descuento_total += descuento
        return descuento_total

    def calcular_despacho(self, tipo_despacho):
        valor_productos = sum(item.cantidad * item.producto.precio for item in self.items)

        if tipo_despacho == 0:  # Despacho Aéreo Normal
            valor_despacho = 0.2 * valor_productos
        elif tipo_despacho == 1:  # Despacho Aéreo Express
            valor_despacho = 0.3 * valor_productos
        else:
            valor_despacho = 0

        return valor_despacho

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            return 0.2
        else:
            return 0

    def checkout(self, tipo_despacho, direccion):
        descuentos = self.calcular_descuentos()
        valor_despacho = self.calcular_despacho(tipo_despacho)
        impuesto = self.calcular_impuesto(direccion)

        valor_productos = sum(item.cantidad * item.producto.precio for item in self.items)
        total_pagar = valor_productos - descuentos + valor_despacho
        total_pagar += impuesto * total_pagar

        return total_pagar
