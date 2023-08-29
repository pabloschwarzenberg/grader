class CarroDeCompras:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.descuento
        return descuentos
    
    def calcular_valor_despacho(self, tipoDespacho):
        valor_productos = sum([producto.precio for producto in self.productos])
        
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            valor_despacho = 0.2 * valor_productos
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            valor_despacho = 0.3 * valor_productos
        else:
            raise ValueError("Tipo de despacho inválido.")
        
        return valor_despacho
    
    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        valor_despacho = self.calcular_valor_despacho(tipoDespacho)
        
        valor_total = sum([producto.precio for producto in self.productos]) - descuentos + valor_despacho
        
        if "chile" in direccion.lower():
            valor_total *= 1.2  # Agregar impuesto del 20%
        
        return valor_total
