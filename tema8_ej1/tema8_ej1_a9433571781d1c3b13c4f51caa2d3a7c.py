class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class CarroCompras:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def calcular_descuentos(self):
        descuento = 0
        for producto in self.productos:
            descuento += producto.precio * 0.1  # 10% de descuento
        return descuento
    
    def calcular_despacho(self, tipoDespacho):
        total_productos = sum(producto.precio for producto in self.productos)
        if tipoDespacho == 0:
            return total_productos * 0.2  # 20% del valor de los productos
        elif tipoDespacho == 1:
            return total_productos * 0.3  # 30% del valor de los productos
    
    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            return 0.2  # 20% de impuesto para despacho a Chile
        else:
            return 0  # Sin impuesto para despachos internacionales
    
    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)
        
        total_productos = sum(producto.precio for producto in self.productos)
        total_pagar = total_productos - descuentos + despacho
        total_pagar += total_pagar * impuesto
        
        return total_pagar


# Ejemplo de uso
producto1 = Producto("Camisa", 25)
producto2 = Producto("Pantalón", 40)

carro = CarroCompras()
carro.agregar_producto(producto1)
carro.agregar_producto(producto2)

tipoDespacho = 0  # Despacho Aéreo Normal
direccion = "Alameda 340 Santiago Chile"

total_pagar = carro.checkout(tipoDespacho, direccion)
print("Total a pagar:", total_pagar)