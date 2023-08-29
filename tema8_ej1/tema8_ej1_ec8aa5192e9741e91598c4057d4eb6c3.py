total = 0

class CarroDeCompras:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def quitarProducto(self, producto):
        self.productos.remove(producto)

    def calcularTotal(self):
        total = 0
        for producto in self.productos:
            total += producto.valor
        return total
        
def checkout(self, descuento, direccion):
    total = self.calcularTotal()
    descuento = 0
    if (len(self.productos) >= 4):
        descuento = total * 0.2
    elif (len(self.productos) == 3):
        descuento = total * 0.1
    else:
        descuento = 0

    total = total - descuento
    if (tipoDespacho == 0):
        total += (total * 0.2)