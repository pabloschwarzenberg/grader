class CarroCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def mostrar_carro(self):
        for producto, cantidad in self.productos:
            print("{} (Producto {}): {} unidades".format(producto, producto, cantidad))

    def checkout(self, tipoDespacho, direccion):
        # Calcular valor de los descuentos
        descuento = 0
        for producto, cantidad in self.productos:
            if producto in (1, 2, 3) and len(self.productos) >= 3:
                descuento += 0.2 * producto
            elif producto in (4, 5) and len(self.productos) >= 2:
                descuento += 0.15 * producto
        despacho = 0
        if tipoDespacho == 0:
            despacho = 0.2 * sum(precio for producto, precio in PRODUCTOS.values())
        elif tipoDespacho == 1:
            despacho = 0.3 * sum(precio for producto, precio in PRODUCTOS.values())

        # Calcular valor total a pagar
        total = sum(precio for producto, precio in PRODUCTOS.values()) - descuento + despacho
        if "chile" in direccion.lower():
            total *= 1.2

        return total


if __name__ == "__main__":
    carro = CarroCompras()
    carro.agregar_producto(1, 2)
    carro.agregar_producto(2, 1)
    carro.agregar_producto(3, 3)
    carro.mostrar_carro()
    total_pagar = carro.checkout(1, "Alameda 340 Santiago Chile")
    print("El total a pagar es: USD {:.1f}".format(total_pagar))

           