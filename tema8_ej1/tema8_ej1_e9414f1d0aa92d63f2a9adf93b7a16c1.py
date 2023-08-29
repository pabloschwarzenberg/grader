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

    def calcular_valor_despacho(self, tipoDespacho):
        valor_productos = sum([producto.precio for producto in self.productos])

        if tipoDespacho == 0:
            return valor_productos * 0.2
        elif tipoDespacho == 1:
            return valor_productos * 0.3
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        valor_despacho = self.calcular_valor_despacho(tipoDespacho)
        valor_total = sum([producto.precio for producto in self.productos]) - descuentos + valor_despacho

        if "Chile" in direccion:
            valor_total += valor_total * 0.2

        return valor_total


class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento


# Ejemplo de uso
if __name__ == "__main__":
    carro = CarroCompras()

    producto1 = Producto("Camiseta", 10000, 500)
    producto2 = Producto("Pantalón", 20000, 1000)
    producto3 = Producto("Zapatillas", 50000, 0)

    carro.agregar_producto(producto1)
    carro.agregar_producto(producto2)
    carro.agregar_producto(producto3)

    tipo_despacho = 1  # Despacho Aéreo Express
    direccion = "Alameda 340 Santiago Chile"

    valor_total = carro.checkout(tipo_despacho, direccion)
    print(f"Total a pagar: {valor_total}")
