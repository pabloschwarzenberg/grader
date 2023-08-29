class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def calcular_descuentos(self):
        descuentos = 0
        for producto in self.productos:
            if producto.descuento:
                descuentos += producto.precio * producto.descuento
        return descuentos

    def calcular_despacho(self, tipoDespacho):
        valor_total = self.calcular_total()
        descuentos = self.calcular_descuentos()

        if tipoDespacho == 0:
            despacho = valor_total * 0.2
        elif tipoDespacho == 1:
            despacho = valor_total * 0.3
        else:
            despacho = 0

        return despacho - descuentos

    def checkout(self, tipoDespacho, direccion):
        valor_total = self.calcular_total()
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)

        if "Chile" in direccion:
            impuesto = valor_total * 0.2
        else:
            impuesto = 0

        total_pagar = valor_total - descuentos + despacho + impuesto
        return total_pagar


class Producto:
    def __init__(self, nombre, precio, descuento=False):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento


# Ejemplo de uso
carro = CarroCompras()

producto1 = Producto("Camiseta", 10000)
producto2 = Producto("Zapatos", 50000, descuento=True)
producto3 = Producto("Pantalón", 8000)

carro.agregar_producto(producto1)
carro.agregar_producto(producto2)
carro.agregar_producto(producto3)

tipoDespacho = 0  # Despacho Aéreo Normal
direccion = "Alameda 340 Santiago Chile"

total_pagar = carro.checkout(tipoDespacho, direccion)
print(f"Total a pagar: {total_pagar}")
