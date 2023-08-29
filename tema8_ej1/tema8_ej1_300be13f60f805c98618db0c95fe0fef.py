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
            despacho = valor_productos * 0.2  # 20% del valor de los productos
        elif tipoDespacho == 1:
            despacho = valor_productos * 0.3  # 30% del valor de los productos
        else:
            despacho = 0  # Tipo de despacho inválido
        return despacho

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        valor_productos = sum([producto.precio for producto in self.productos])
        
        if "chile" in direccion.lower():
            impuesto = valor_productos * 0.2  # 20% de impuesto
        else:
            impuesto = 0
        
        valor_total = valor_productos - descuentos + despacho + impuesto
        return valor_total
