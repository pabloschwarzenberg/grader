class Producto:
    def __init__(self, codigo, nombre, stock, precio):
        self.codigo = codigo
        self.stock = stock
        self.precio = precio
        self.nombre = nombre
    def __eq__(self, other):
        if self.codigo == other.codigo:
            return True
        else:
            return False
class Item:
    def __init__(self, cantidad, producto):
        self.cantidad = cantidad
        self.producto = producto
class Carro:
    def __init__(self):
        self.lista_de_productos = []
        self.descuento = 0
        self.total = 0
        self.direccion = ""
    def agregar_item(self, cantidad, producto):
        for item in self.lista_de_productos:
            if item.producto == producto:
                if cantidad == 0:
                    self.lista_de_productos.remove(item)
                else:
                    item.cantidad = cantidad
                return
        item = Item(cantidad, producto)
        self.lista_de_productos.append(item)
    def calcular_descuento(self):
        total_descuento = 0
        for item in self.lista_de_productos:
            descuento = item.producto.precio * 0.2
            total_descuento += descuento * item.cantidad
        return total_descuento
    def calcular_despacho(self, tipoDespacho):
        total_productos = self.total - self.descuento
        if tipoDespacho == 0:
            return total_productos * 0.2
        elif tipoDespacho == 1:
            return total_productos * 0.3

    def calcular_impuesto(self):
        if "Chile" in self.direccion or "chile" in self.direccion:
            return self.total * 0.2
        else:
            return 0
    def checkout(self, tipoDespacho, direccion):
        self.direccion = direccion
        self.descuento = self.calcular_descuento()
        self.total = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
        total_despacho = self.calcular_despacho(tipoDespacho)
        impuesto = self.calcular_impuesto()

        subtotal = self.total - self.descuento + total_despacho
        if "Chile" in direccion or "chile" in direccion:
            subtotal += subtotal * 0.2

        total_pagar = round(subtotal)
        total_pagar_float = int(total_pagar)

        return total_pagar_float


    def __repr__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s += "{0}: {1}\n".format(item.cantidad, item.producto.nombre)
        return s

class Tienda:
    def __init__(self):
        self.catalogo = []
        producto = Producto(1, "Juego Pokemon Y", 10, 31.51)
        self.catalogo.append(producto)
        producto = Producto(2, "Nintendo 3DS", 5, 190.95)
        self.catalogo.append(producto)
        producto = Producto(3, "Juego Mario Kart", 10, 29.96)
        self.catalogo.append(producto)
        producto = Producto(4, "Playstation 4", 10, 399)
        self.catalogo.append(producto)
        producto = Producto(5, "Fifa 14", 10, 41.95)
        self.catalogo.append(producto)

    def menu(self):
        for producto in self.catalogo:
            print("{0}: {1} ${2}".format(producto.codigo, producto.nombre, producto.precio))

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
    print(carro.checkout(0, "chile"))
    print(carro.checkout(1, "Chile"))