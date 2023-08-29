class CarroCompras:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.calcular_descuento()
        return descuentos
    
    def calcular_despacho(self, tipoDespacho):
        valor_productos = self.calcular_valor_productos()
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return 0.2 * valor_productos
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return 0.3 * valor_productos
    
    def calcular_valor_productos(self):
        valor_total = 0
        for producto in self.productos:
            valor_total += producto.precio
        return valor_total
    
    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        valor_productos = self.calcular_valor_productos()
        
        if "chile" in direccion.lower():
            impuesto = 0.2 * valor_productos
        else:
            impuesto = 0
        
        valor_total = valor_productos - descuentos + despacho + impuesto
        return valor_total


class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
    
    def calcular_descuento(self):
        return self.precio * self.descuento


# Ejemplo de uso
carro = CarroCompras()

producto1 = Producto("Camiseta", 20000, 0.1)
producto2 = Producto("Pantalón", 30000, 0.2)
producto3 = Producto("Zapatos", 50000, 0.15)

carro.agregar_producto(producto1)
carro.agregar_producto(producto2)
carro.agregar_producto(producto3)

tipoDespacho = 0  # Despacho Aéreo Normal
direccion = "Alameda 340 Santiago Chile"

valor_total = carro.checkout(tipoDespacho, direccion)
print("Valor total a pagar:", valor_total)
