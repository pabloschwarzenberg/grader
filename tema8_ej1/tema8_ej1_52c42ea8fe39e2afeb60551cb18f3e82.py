class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento


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

    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum(producto.precio for producto in self.productos)
        if tipoDespacho == 0:
            despacho = 0.2 * valor_productos  # 20% del valor de los productos
        elif tipoDespacho == 1:
            despacho = 0.3 * valor_productos  # 30% del valor de los productos
        else:
            despacho = 0
        return despacho

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)

        valor_productos = sum(producto.precio for producto in self.productos)
        total_pagar = valor_productos - descuentos + despacho

        if "chile" in direccion.lower():
            total_pagar *= 1.2  # Agregar 20% por impuestos para despachos a Chile

        return total_pagar


# Ejemplo de uso
carrito = CarroDeCompras()

# Agregar productos al carrito
producto1 = Producto("Camisa", 100, 10)
producto2 = Producto("Pantalón", 150, 20)
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

total_a_pagar = carrito.checkout(0, "Alameda 340 Santiago Chile")
print("Total a pagar:", total_a_pagar)
