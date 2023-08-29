import modulo

class CarroDeCompras:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.precio * producto.descuento
        return descuentos
    
    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum(producto.precio for producto in self.productos)
        if tipoDespacho == 0:
            return valor_productos * 0.2
        elif tipoDespacho == 1:
            return valor_productos * 0.3
        else:
            return 0
    
    def calcular_impuesto(self, direccion):
        if 'chile' in direccion.lower():
            return 0.2
        else:
            return 0
    
    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)
        
        valor_productos = sum(producto.precio for producto in self.productos)
        total_pagar = valor_productos - descuentos + despacho
        if impuesto > 0:
            total_pagar += total_pagar * impuesto
        
        return total_pagar

# Ejemplo de uso
mi_carro = CarroDeCompras()
mi_carro.agregar_producto(modulo.Producto("Producto 1", 10, 0.1))
mi_carro.agregar_producto(modulo.Producto("Producto 2", 20, 0.2))

total_a_pagar = mi_carro.checkout(0, "Alameda 340 Santiago Chile")
print("Total a pagar:", total_a_pagar)

