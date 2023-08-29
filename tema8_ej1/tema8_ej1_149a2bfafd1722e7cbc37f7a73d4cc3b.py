class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio


class Carro:
    def __init__(self):
        self.items = []

    def agregar_item(self, cantidad, producto):
        self.items.append((cantidad, producto))

    def __str__(self):
        carro_str = ""
        for cantidad, producto in self.items:
            carro_str += f"{producto.nombre} x{cantidad}\n"
        return carro_str

    def calcular_total(self):
        total = 0
        for cantidad, producto in self.items:
            total += cantidad * producto.precio
        return total

    def calcular_descuentos(self):
        total = self.calcular_total()
        descuentos = 0
        for cantidad, producto in self.items:
            descuento = cantidad * producto.precio * 0.1
            descuentos += descuento
        return descuentos

    def calcular_despacho(self, tipoDespacho):
        total = self.calcular_total()
        descuentos = self.calcular_descuentos()
        despacho = 0
        if tipoDespacho == 0:
            despacho = total * 0.2
        elif tipoDespacho == 1:
            despacho = total * 0.3
        return despacho - descuentos

    def calcular_impuesto(self, direccion):
        if "chile" in direccion.lower():
            total = self.calcular_total()
            descuentos = self.calcular_descuentos()
            impuesto = (total - descuentos) * 0.2
            return impuesto
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        total = self.calcular_total()
        descuentos = self.calcular_descuentos()
        despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto(direccion)
        total_pagar = total - descuentos + despacho + impuesto
        return total_pagar


class Tienda:
    def __init__(self):
        self.catalogo = [
            Producto(1, "Producto 1", 100),
            Producto(2, "Producto 2", 200),
            Producto(3, "Producto 3", 300),
        ]

    def menu(self):
        for producto in self.catalogo:
            print("{0}: {1} ${2}".format(
                producto.codigo, producto.nombre, producto.precio))

    def buscarProducto(self, numero):
        for producto in self.catalogo:
            if producto.codigo == numero:
                return producto


if __name__ == "__main__":
    tienda = Tienda()
    carro = Carro()

    while True:
        tienda.menu()
        item_ingresado = input("Ingresa un producto a comprar (numero,cantidad): ")
        if item_ingresado == "":
            break
        else:
            item_ingresado = item_ingresado.split(",")
            numero = int(item_ingresado[0])
            producto = tienda.buscarProducto(numero)
            cantidad = int(item_ingresado[1])
            carro.agregar_item(cantidad, producto)

    print(carro)
    print(carro.checkout(0, "usa"))
    print(carro.checkout(1, "usa"))
    print(carro.checkout(0, "Alameda 340 Santiago Chile"))
    print(carro.check
