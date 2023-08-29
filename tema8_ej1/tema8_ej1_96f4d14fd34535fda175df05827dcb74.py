class Carro:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            if producto['descuento']:
                descuentos += producto['precio'] * producto['descuento'] / 100
        return descuentos

    def calcular_valor_productos(self):
        valor_productos = 0
        for producto in self.productos:
            valor_productos += producto['precio']
        return valor_productos

    def calcular_despacho(self, tipoDespacho):
        valor_productos = self.calcular_valor_productos()
        if tipoDespacho == 0:
            return valor_productos * 0.2
        elif tipoDespacho == 1:
            return valor_productos * 0.3
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        valor_total = self.calcular_valor_productos() - descuentos + despacho
        if 'chile' in direccion.lower():
            valor_total *= 1.2
        return valor_total

carro = Carro()
carro.agregar_producto({'nombre': 'producto1', 'precio': 100, 'descuento': 10})
carro.agregar_producto({'nombre': 'producto2', 'precio': 200, 'descuento': 20})
carro.agregar_producto({'nombre': 'producto3', 'precio': 300, 'descuento': 0})

valor_total = carro.checkout(0, 'Alameda 340 Santiago Chile')
print(valor_total)
