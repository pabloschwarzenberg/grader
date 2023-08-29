class CarroCompras:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.descuento
        return descuentos
    
    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum([producto.precio for producto in self.productos])
        if tipoDespacho == 0:
            return 0.2 * valor_productos
        elif tipoDespacho == 1:
            return 0.3 * valor_productos
        else:
            return 0
    
    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        valor_despacho = self.calcular_despacho(tipoDespacho)
        valor_total = sum([producto.precio for producto in self.productos]) - descuentos + valor_despacho
        
        if 'chile' in direccion.lower():
            valor_total *= 1.2
        
        return valor_total


class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento


# Ejemplo de uso
producto1 = Producto("Camisa", 25000, 5000)
producto2 = Producto("Pantalón", 50000, 10000)
producto3 = Producto("Zapatos", 80000, 0)

carro = CarroCompras()
carro.agregar_producto(producto1)
carro.agregar_producto(producto2)
carro.agregar_producto(producto3)

valor_total = carro.checkout(1, "Alameda 340 Santiago Chile")
print(f"Valor total a pagar: ${valor_total}")
