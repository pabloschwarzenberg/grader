class CarroDeCompras:
    def __init__(self):
        self.productos = {}
        self.descuentos = {}
    def agregarProducto(self, producto, precio):
        if producto in self.productos:
            self.productos[producto] += precio
        else:
            self.productos[producto] = precio
    def agregarDescuento(self, producto, descuento):
        if producto in self.productos:
            self.descuentos[producto] = descuento
        else:
            raise ValueError("El producto no está en el carro de compras")
    def quitarProducto(self, producto):
        if producto in self.productos:
            del self.productos[producto]
            if producto in self.descuentos:
                del self.descuentos[producto]
        else:
            raise ValueError("El producto no está en el carro de compras")
    def calcularDescuentos(self):
        total_descuentos = 0
        for producto, precio in self.productos.items():
            if producto in self.descuentos:
                total_descuentos += (precio * self.descuentos[producto])
        return total_descuentos
    
    def calcularDespacho(self, tipoDespacho):
        total_productos = sum(self.productos.values())
        if tipoDespacho == 0:
            valor_despacho = total_productos * 0.2
        elif tipoDespacho == 1:
            valor_despacho = total_productos * 0.3
        else:
            raise ValueError("Tipo de despacho inválido. Use 0 para despacho normal o 1 para despacho express.")
        return valor_despacho
    
    def checkout(self, tipoDespacho, direccion=None):
        total_productos = sum(self.productos.values())
        descuentos = self.calcularDescuentos()
        valor_despacho = self.calcularDespacho(tipoDespacho)
        valor_total = total_productos - descuentos + valor_despacho
        if direccion and "chile" in direccion.lower():
            valor_total *= 1.2
        return valor_total