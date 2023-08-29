class Carro:
    def __init__(self):
        self.lista_de_productos = []
        self.descuento = 0
        self.total = 0
        self.direccion = ""

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

    def checkout(self, tipoDespacho, direccion):
        # Calcular descuentos
        for item in self.lista_de_productos:
            self.descuento += item.producto.precio * item.cantidad

        # Calcular valor de despacho
        if tipoDespacho == 0:
            despacho = self.descuento * 0.2
        elif tipoDespacho == 1:
            despacho = self.descuento * 0.3
        else:
            return "Tipo de despacho inválido"

        # Calcular valor total
        if "Chile" in direccion:
            self.total = self.descuento - despacho + self.descuento * 0.2
        else:
            self.total = self.descuento - despacho

        return self.total

    def __repr__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s += "{0}: {1}\n".format(item.cantidad, item.producto.nombre)
        return s

carro = Carro()
carro.agregar_item(2, tienda.buscarProducto(1))
carro.agregar_item(1, tienda.buscarProducto(2))
print(carro.checkout(0, "Alameda 340 Santiago Chile"))