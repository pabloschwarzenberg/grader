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
        self.despacho = 0
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

    def calcular_descuentos(self):
        self.descuento = sum(
            item.producto.precio * item.cantidad * 0.1
            for item in self.lista_de_productos
            if item.cantidad >= 3
        )

    def calcular_despacho(self, tipoDespacho):
        valor_productos = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            self.despacho = valor_productos * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            self.despacho = valor_productos * 0.3
        else:
            self.despacho = 0

    def checkout(self, tipoDespacho, direccion):
        self.calcular_descuentos()
        self.calcular_despacho(tipoDespacho)

        total_productos = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
        total_descuentos = self.descuento
        total_despacho = self.despacho

        if "chile" in direccion.lower():
            impuesto = (total_productos - total_descuentos + total_despacho) * 0.2
        else:
            impuesto = 0

        self.total = total_productos - total_descuentos + total_despacho + impuesto
        return self.total

    def __repr__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s = s + "{0}: {1}\n".format(item.cantidad, item.producto.nombre)
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
        producto = Producto(5, "Fifa 14", 10, 19.99)
        self.catalogo.append(producto)


tienda = Tienda()
carro = Carro()

# Agregar productos al carro
carro.agregar_item(1, tienda.catalogo[0])
carro.agregar_item(2, tienda.catalogo[1])
carro.agregar_item(3, tienda.catalogo[2])

# Realizar el checkout
tipoDespacho = 0  # Despacho Aéreo Normal
direccion = "USA"
total_pagar = carro.checkout(tipoDespacho, direccion)

print(f"Total a pagar: {total_pagar}")
