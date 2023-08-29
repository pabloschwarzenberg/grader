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
            return valor_productos * 0.2  # 20% del valor de los productos
        elif tipoDespacho == 1:
            return valor_productos * 0.3  # 30% del valor de los productos
        else:
            return 0

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            return 0.2  # 20% de impuesto para envíos a Chile
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        valor_despacho = self.calcular_valor_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)

        valor_productos = sum([producto.precio for producto in self.productos])
        valor_total = valor_productos - descuentos + valor_despacho
        valor_total += valor_total * impuesto

        return valor_total
