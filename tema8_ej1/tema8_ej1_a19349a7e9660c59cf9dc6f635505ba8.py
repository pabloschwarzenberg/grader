class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Carro:
    def __init__(self):
        self.items = []
        self.modulo = modulo  # Reemplaza 'modulo' con el nombre real del módulo que contiene la clase Tienda

    def agregar_item(self, cantidad, producto):
        self.items.append((cantidad, producto))

    def calcular_descuentos(self):
        descuentos = 0
        for cantidad, producto in self.items:
            descuentos += producto.precio * cantidad * 0.1  # Supongamos que hay un descuento del 10% en todos los productos
        return descuentos

    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum(producto.precio * cantidad for cantidad, producto in self.items)
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return valor_productos * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return valor_productos * 0.3

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            return 0.2
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)

        valor_productos = sum(producto.precio * cantidad for cantidad, producto in self.items)
        total_pagar = valor_productos - descuentos + despacho
        if impuesto > 0:
            total_pagar *= (1 + impuesto)

        return total_pagar

if __name__ == "__main__":
    producto1 = Producto(1, "Camiseta", 2, 20.0)
    producto2 = Producto(2, "Pantalón", 1, 30.0)
    producto3 = Producto(3, "Zapatos", 1, 50.0)

    carro = Carro()
    carro.agregar_item(2, producto1)
    carro.agregar_item(1, producto2)
    carro.agregar_item(1, producto3)

    print(carro.checkout(0, "usa"))  # Despacho Aéreo Normal hacia USA
    print(carro.checkout(1, "usa"))  # Despacho Aéreo Express hacia USA
    print(carro.checkout(0, "Alameda 340 Santiago Chile"))  # Despacho Aéreo Normal hacia Chile
