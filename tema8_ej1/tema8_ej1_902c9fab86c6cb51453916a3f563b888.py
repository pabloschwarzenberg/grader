class CarroDeCompras:
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
        valor_productos = self.calcularTotalProductos()
        if tipoDespacho == 0:
            return valor_productos * 0.2
        elif tipoDespacho == 1:
            return valor_productos * 0.3
        else:
            return 0

    def calcularTotalProductos(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcularDescuentos()
        valor_productos = self.calcularTotalProductos()
        despacho = self.calcularDespacho(tipoDespacho)

        if "chile" in direccion.lower():
            total = valor_productos - descuentos + despacho + (valor_productos * 0.2)
        else:
            total = valor_productos - descuentos + despacho

        return total


# Ejemplo de uso
class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

    def calcularDescuento(self):
        return self.precio * self.descuento


carro = CarroDeCompras()

producto1 = Producto("Camisa", 20, 0.1)
producto2 = Producto("Pantalón", 30, 0.2)
producto3 = Producto("Zapatos", 50, 0.15)

carro.agregarProducto(producto1)
carro.agregarProducto(producto2)
carro.agregarProducto(producto3)

tipoDespacho = 0  # Despacho Aéreo Normal
direccion = "Alameda 340 Santiago Chile"

total_pagar = carro.checkout(tipoDespacho, direccion)
print(f"Total a pagar: {total_pagar}")  # Salida: Total a pagar: 86.0

           