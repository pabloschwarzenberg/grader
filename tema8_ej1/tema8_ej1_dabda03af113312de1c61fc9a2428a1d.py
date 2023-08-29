class CarroDeCompras:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularDescuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.precio * (producto.descuento / 100)
        return descuentos

    def calcularDespacho(self, tipoDespacho):
        valor_productos = sum(producto.precio for producto in self.productos)
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return valor_productos * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return valor_productos * 0.3
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcularDescuentos()
        despacho = self.calcularDespacho(tipoDespacho)
        total = sum(producto.precio for producto in self.productos) - descuentos + despacho

        if "Chile" in direccion:
            total += total * 0.2

        return total
