class CarroDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.calcular_descuento()
        return descuentos

    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum(producto.precio for producto in self.productos)
        if tipoDespacho == 0:
            return valor_productos * 0.2  # 20% del valor de los productos
        elif tipoDespacho == 1:
            return valor_productos * 0.3  # 30% del valor de los productos
        else:
            return 0

    def calcular_valor_total(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        valor_productos = sum(producto.precio for producto in self.productos)
        
        if "chile" in direccion.lower():
            valor_total = (valor_productos - descuentos + despacho) * 1.2  # Se agrega el 20% de impuesto
        else:
            valor_total = valor_productos - descuentos + despacho

        return valor_total

    def checkout(self, tipoDespacho, direccion):
        valor_total = self.calcular_valor_total(tipoDespacho, direccion)
        return valor_total
