class CarroDeCompras:
    def __init__(self):
        self.productos = []
        self.modulo = __import__('modulo')

    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.descuento
        return descuentos

    def calcular_valor_despacho(self, tipoDespacho):
        valor_productos = sum([producto.precio for producto in self.productos])
        if tipoDespacho == 0:
            return 0.2 * valor_productos  
        elif tipoDespacho == 1:
            return 0.3 * valor_productos 

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            return 0.2
        return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        valor_despacho = self.calcular_valor_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)

        valor_productos = sum([producto.precio for producto in self.productos])
        total_pagar = valor_productos - descuentos + valor_despacho
        total_pagar += impuesto * (total_pagar - valor_despacho)

        return total_pagar