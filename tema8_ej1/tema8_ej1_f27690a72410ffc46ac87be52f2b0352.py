class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularDescuentos(self):
        descuentos = 0
        for producto in self.productos:
            descuentos += producto.calcularDescuento()
        return descuentos

    def calcularDespacho(self, tipoDespacho):
        valor_productos = sum([producto.precio for producto in self.productos])
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            return 0.2 * valor_productos
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            return 0.3 * valor_productos
        else:
            return 0

    def calcularImpuesto(self, direccion):
        if "chile" in direccion.lower():
            return 0.2
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcularDescuentos()
        despacho = self.calcularDespacho(tipoDespacho)
        impuesto = self.calcularImpuesto(direccion)

        valor_productos = sum([producto.precio for producto in self.productos])

        total_pagar = valor_productos - descuentos + despacho
        total_pagar += impuesto * total_pagar

        return total_pagar


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcularDescuento(self):
        return 0  # Cálculo del descuento para cada producto


# Ejemplo de uso
carro = CarroCompras()

producto1 = Producto("Camisa", 20)
producto2 = Producto("Pantalón", 30)
producto3 = Producto("Zapatos", 50)

carro.agregarProducto(producto1)
carro.agregarProducto(producto2)
carro.agregarProducto(producto3)

tipo_despacho = 0  # Despacho Aéreo Normal
direccion_despacho = "Alameda 340 Santiago Chile"

total_pagar = carro.checkout(tipo_despacho, direccion_despacho)
print("Total a pagar:", total_pagar)
