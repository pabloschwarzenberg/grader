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
        total_productos = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
        if total_productos >= 100:
            self.descuento = total_productos * 0.1

    def calcular_valor_despacho(self, tipoDespacho):
        total_productos = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
        if tipoDespacho == 0:
            return total_productos * 0.2
        elif tipoDespacho == 1:
            return total_productos * 0.3
        else:
            return 0

    def calcular_impuesto(self):
        if "chile" in self.direccion.lower():
            return self.total * 0.2
        else:
            return 0

    def checkout(self, tipoDespacho, direccion):
        self.calcular_descuento()
        self.direccion = direccion
        valor_despacho = self.calcular_valor_despacho(tipoDespacho)
        self.total = sum(item.producto.precio * item.cantidad for item in self.lista_de_productos)
        self.total -= self.descuento
        self.total += valor_despacho
        impuesto = self.calcular_impuesto()
        self.total += impuesto
        return self.total

    def __repr__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s += f"{item.cantidad}: {item.producto.nombre}\n"
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
            print(f"{producto.codigo}: {producto.nombre} ${producto.precio}")

    def agregar_al_carro(self, carro, codigo, cantidad):
        for producto in self.catalogo:
            if producto.codigo == codigo:
                if cantidad <= producto.stock:
                    carro.agregar_item(cantidad, producto)
                    producto.stock -= cantidad
                    print("Producto agregado al carro de compras.")
                    return
                else:
                    print("No hay suficiente stock.")
                    return
        print("Código de producto inválido.")

if __name__ == "__main__":
    tienda = Tienda()
    carro = Carro()
    tienda.menu()
    tienda.agregar_al_carro(carro, 1, 2)
    tienda.agregar_al_carro(carro, 2, 1)
    tienda.agregar_al_carro(carro, 3, 3)
    total = carro.checkout(0, "Alameda 340 Santiago Chile")
    print(f"Total a pagar: {total}")



