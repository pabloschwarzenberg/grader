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
        item = item(cantidad, producto)
        self.lista_de_productos.append(item)

    def calcular_descuentos(self):
        valor_productos = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
        self.descuento = 0.1 * valor_productos  # Descuento del 10% del valor total de los productos

    def calcular_valor_despacho(self, tipoDespacho):
        valor_productos = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)

        if tipoDespacho == 0:
            valor_despacho = 0.2 * valor_productos  # Despacho Aéreo Normal: 20% del valor de los productos
        elif tipoDespacho == 1:
            valor_despacho = 0.3 * valor_productos  # Despacho Aéreo Express: 30% del valor de los productos
        else:
            raise ValueError("Tipo de despacho inválido")

        return valor_despacho

    def checkout(self, tipoDespacho, direccion):
        self.calcular_descuentos()
        valor_despacho = self.calcular_valor_despacho(tipoDespacho)

        valor_productos = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
        valor_total = valor_productos - self.descuento + valor_despacho

        if "chile" in direccion.lower():
            valor_total *= 1.2  # Impuesto del 20% para despachos a Chile

        self.total = valor_total
        self.direccion = direccion

        return valor_total
