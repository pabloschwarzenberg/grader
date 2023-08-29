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
        valor_productos = sum(producto.precio for producto in self.productos)
        if tipoDespacho == 0:
            return valor_productos * 0.2
        elif tipoDespacho == 1:
            return valor_productos * 0.3
        else:
            return 0

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            return 0.2
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)
        valor_productos = sum(producto.precio for producto in self.productos)

        total_pagar = valor_productos - descuentos + despacho
        total_pagar *= (1 + impuesto)

        return total_pagar


class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento


if __name__ == "__main__":
    carro = CarroCompras()

    producto1 = Producto("Camiseta", 1000, 100)
    producto2 = Producto("Pantalón", 2000, 150)

    carro.agregar_producto(producto1)
    carro.agregar_producto(producto2)

    tipo_despacho = 0
    direccion_despacho = "Alameda 340 Santiago Chile"

    total_pagar = carro.checkout(tipo_despacho, direccion_despacho)
    print("Total a pagar:", total_pagar)
