class CarroDeCompras:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def calcular_total(self):
        subtotal = sum([producto.precio for producto in self.productos])
        
        # Calcular descuentos
        descuentos = 0
        for producto in self.productos:
            if producto.categoria == "alimentos":
                descuentos += producto.precio * 0.1
            elif producto.categoria == "ropa" and producto.precio > 10000:
                descuentos += producto.precio * 0.2
        
        # Calcular despacho
        if tipoDespacho == 0:
            despacho = subtotal * 0.2
        elif tipoDespacho == 1:
            despacho = subtotal * 0.3
        else:
            despacho = 0
        
        # Calcular impuestos
        if "chile" in direccion.lower():
            impuestos = (subtotal - descuentos + despacho) * 0.2
        else:
            impuestos = 0
        
        # Calcular total a pagar
        total = subtotal - descuentos + despacho + impuestos
        return total

    def checkout(self, tipoDespacho, direccion):
        total = self.calcular_total()
        return total
