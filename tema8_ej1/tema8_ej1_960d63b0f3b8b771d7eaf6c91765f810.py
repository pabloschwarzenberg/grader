class Carro:
    def __init__(self):
        self.lista_de_productos=[]
        self.descuento=0
        self.total=0
        self.direccion=""

    def agregar_item(self, cantidad, producto):
        for item in self.lista_de_productos:
            if item.producto == producto:
                if cantidad == 0:
                    self.lista_de_productos.remove(item)
                else:
                    item.cantidad = cantidad
                return
        item = Item(cantidad, producto)
        self.lista_de_productos.append(item)

    def calcular_descuentos(self):
        self.descuento = 0
        for item in self.lista_de_productos:
            self.descuento += item.cantidad * item.producto.precio * 0.1  # 10% de descuento por producto

    def calcular_despacho(self, tipoDespacho):
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return self.total * 0.2  # 20% del valor de los productos
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return self.total * 0.3  # 30% del valor de los productos
        else:
            return 0

    def calcular_impuesto(self):
        if "chile" in self.direccion.lower():  # Si el despacho es hacia Chile
            return self.total * 0.2  # 20% de impuesto
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        self.direccion = direccion
        self.calcular_descuentos()
        self.total = 0
        for item in self.lista_de_productos:
            self.total += item.cantidad * item.producto.precio
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto()
        total_pagar = self.total - self.descuento + despacho + impuesto
        return total_pagar

    def __repr__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s = s + "{0}: {1}\n".format(item.cantidad, item.producto.nombre)
        return s