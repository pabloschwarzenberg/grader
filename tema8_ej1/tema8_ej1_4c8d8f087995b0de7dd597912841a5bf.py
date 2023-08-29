class Carro:
    def __init__(self):
        self.productos = []
        self.descuentos = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_descuentos(self):
        # Calcular descuentos basados en los productos en el carro
        pass

    def checkout(self, tipoDespacho, direccion):
        self.calcular_descuentos()
        valor_productos = sum(p.precio for p in self.productos)
        if tipoDespacho == 0:
            valor_despacho = valor_productos * 0.2
        elif tipoDespacho == 1:
            valor_despacho = valor_productos * 0.3
        else:
            print('Tipo de despacho inválido')
            return
        valor_total = valor_productos - self.descuentos + valor_despacho
        if 'chile' in direccion.lower():
            valor_total *= 1.2
        return valor_total


# Ejemplo de uso
if __name__ == "__main__":
    carro = Carro()

    # Agregar productos al carro
    producto1 = Producto("Producto 1", 10)
    producto2 = Producto("Producto 2", 20)
    carro.agregar_producto(producto1)
    carro.agregar_producto(producto2)

    # Realizar checkout
    tipoDespacho = 0  # Despacho Aéreo Normal
    direccion = "Alameda 340 Santiago Chile"
    total_a_pagar = carro.checkout(tipoDespacho, direccion)
    print("Total a pagar:", total_a_pagar)
