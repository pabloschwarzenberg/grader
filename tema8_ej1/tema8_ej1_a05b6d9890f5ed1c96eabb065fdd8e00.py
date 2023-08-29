class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularDescuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.precio * producto.descuento
        return descuentos

    def calcularDespacho(self, tipoDespacho):
        valorProductos = sum([producto.precio for producto in self.productos])
        if tipoDespacho == 0:
            return valorProductos * 0.2  # Despacho Aéreo Normal
        elif tipoDespacho == 1:
            return valorProductos * 0.3  # Despacho Aéreo Express

    def calcularImpuesto(self, direccion):
        if 'Chile' in direccion:
            return 0.2
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcularDescuentos()
        despacho = self.calcularDespacho(tipoDespacho)
        impuesto = self.calcularImpuesto(direccion)

        valorProductos = sum([producto.precio for producto in self.productos])
        total = valorProductos - descuentos + despacho
        total += total * impuesto

        return total


class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento


# Ejemplo de uso
carro = CarroCompras()

producto1 = Producto("Camiseta", 10000, 0.1)
producto2 = Producto("Pantalón", 20000, 0.2)

carro.agregarProducto(producto1)
carro.agregarProducto(producto2)

tipoDespacho = 1
direccion = "Alameda 340 Santiago Chile"

total = carro.checkout(tipoDespacho, direccion)
print(f"Total a pagar: ${total}")
