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
        valor_productos = 0

        # Calcular valor de los productos y aplicar descuentos
        for item in self.lista_de_productos:
            valor_productos += item.cantidad * item.producto.precio

        if valor_productos >= 100:
            self.descuento = valor_productos * 0.1
        elif valor_productos >= 50:
            self.descuento = valor_productos * 0.05

        # Calcular valor de despacho
        if tipoDespacho == 0:
            valor_despacho = valor_productos * 0.2
        elif tipoDespacho == 1:
            valor_despacho = valor_productos * 0.3
        else:
            valor_despacho = 0

        # Calcular valor total a pagar
        self.total = valor_productos - self.descuento + valor_despacho

        # Aplicar impuesto si el despacho es hacia Chile
        if "chile" in direccion.lower():
            impuesto = self.total * 0.2
            self.total += impuesto

        return self.total

    def __repr__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s = s + "{0}: {1}\n".format(item.cantidad, item.producto.nombre)
        return s        