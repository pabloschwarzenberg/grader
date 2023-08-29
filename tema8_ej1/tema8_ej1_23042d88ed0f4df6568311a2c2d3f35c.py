class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.calcular_descuento()
        return descuentos

    def calcular_despacho(self, tipoDespacho):
        total = self.calcular_total()
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return total * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return total * 0.3
        else:
            return 0

    def calcular_impuesto(self, direccion):
        if 'chile' in direccion.lower():
            return 0.2
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        total = self.calcular_total() - descuentos + despacho
        impuesto = self.calcular_impuesto(direccion)
        total += total * impuesto
        return total


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_descuento(self):
        # Lógica para calcular el descuento del producto
        return 0.1 * self.precio


if __name__ == "__main__":
    carro = CarroCompras()
    producto1 = Producto('Camisa', 20000)
    producto2 = Producto('Pantalón', 30000)
    carro.agregar_producto(producto1)
    carro.agregar_producto(producto2)

    tipoDespacho = 0  # Despacho Aéreo Normal
    direccion = 'Alameda 340 Santiago Chile'
    total_pagar = carro.checkout(tipoDespacho, direccion)
    print('Total a pagar:', total_pagar)
