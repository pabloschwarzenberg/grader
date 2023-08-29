class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def calcularDescuentos(self):
        total_descuentos = 0
        for producto in self.productos:
            descuento = producto.precio * producto.descuento / 100
            total_descuentos += descuento
        return total_descuentos

    def calcularDespacho(self, tipoDespacho):
    
# Crear un objeto CarroCompras
carro = CarroCompras()

# Crear algunos productos
producto1 = Producto("Camiseta", 20, 10)  # Nombre: Camiseta, Precio: $20, Descuento: 10%
producto2 = Producto("Pantalón", 50, 20)  # Nombre: Pantalón, Precio: $50, Descuento: 20%

# Agregar los productos al carro
carro.agregarProducto(producto1)
carro.agregarProducto(producto2)

# Realizar el checkout con tipo de despacho 0 (Despacho Aéreo Normal) y dirección en Chile
total_pagar = carro.checkout(0, "Alameda 340 Santiago Chile")

# Mostrar el total a pagar
print("Total a pagar:", total_pagar)

        total_productos = sum([producto.precio for producto in self.productos])
        if tipoDespacho == 0:
            return 0.2 * total_productos  # Despacho Aéreo Normal: 20% del valor de los productos
        elif tipoDespacho == 1:
            return 0.3 * total_productos  # Despacho Aéreo Express: 30% del valor de los productos
        else:
            return 0  # Tipo de despacho no válido

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcularDescuentos()
        despacho = self.calcularDespacho(tipoDespacho)
        total_productos = sum([producto.precio for producto in self.productos])
        impuesto = 0

        if "chile" in direccion.lower():
            impuesto = 0.2 * total_productos

        total_pagar = total_productos - descuentos + despacho + impuesto
        return total_pagar


class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
