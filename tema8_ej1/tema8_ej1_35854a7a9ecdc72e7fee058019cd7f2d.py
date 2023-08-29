class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Bienvenido a", self.nombre)


class CarroDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        for producto in self.productos:
            print(producto)

    def checkout(self, tipoDespacho, direccion):
        total_productos = sum(producto.precio for producto in self.productos)
        descuentos = total_productos * 0.1
        if tipoDespacho == 0:
            valor_despacho = total_productos * 0.2
        elif tipoDespacho == 1:
            valor_despacho = total_productos * 0.3
        else:
            valor_despacho = 0

        if "chile" in direccion.lower():
            valor_despacho += valor_despacho * 0.2

        valor_total = total_productos - descuentos + valor_despacho
        return valor_total


if __name__ == "__main__":
    tienda_i = Tienda("Mi Tienda")
    tienda_i.saludar()

    carro = CarroDeCompras()

    producto1 = Producto("Camiseta", 100)
    producto2 = Producto("Pantalón", 200)
    producto3 = Producto("Zapatos", 300)

    carro.agregar_producto(producto1)
    carro.agregar_producto(producto2)
    carro.agregar_producto(producto3)

    carro.listar_productos()

    valor_total = carro.checkout(0, "Alameda 340 Santiago Chile")
    print("Valor total a pagar:", valor_total)