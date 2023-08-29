class Producto:
    def __init__(self,codigo,nombre,stock,precio):
        self.codigo=codigo
        self.stock=stock
        self.precio=precio
        self.nombre=nombre

    def __eq__(self,other):
        if self.codigo == other.codigo:
            return True
        else:
            return False

class Item:
    def __init__(self,cantidad,producto):
        self.cantidad=cantidad
        self.producto=producto

class Carro:
    def __init__(self):
        self.lista_de_productos=[]
        self.descuento=0
        self.total=0
        self.direccion=""

    def agregar_item(self,cantidad,producto):
        for item in self.lista_de_productos:
            if item.producto == producto:
                if cantidad==0:
                    self.lista_de_productos.remove(item)
                else:
                    item.cantidad=cantidad
                return
        item=Item(cantidad,producto)
        self.lista_de_productos.append(item)

    def checkout(self,tipoDespacho,direccion):
        return self.total

    def __repr__(self):
        s="Carro de Compras:\n"
        for item in self.lista_de_productos:
            s=s+"{0}: {1}\n".format(item.cantidad,item.producto.nombre)
        return s

class Tienda:
    def  __init__(self):
        self.catalogo=[]
        producto=Producto(1,"Juego Pokemon Y",10,31.51)
        self.catalogo.append(producto)
        producto=Producto(2,"Nintendo 3DS",5,190.95)
        self.catalogo.append(producto)
        producto=Producto(3,"Juego Mario Kart",10,29.96)
        self.catalogo.append(producto)
        producto=Producto(4,"Playstation 4",10,399)
        self.catalogo.append(producto)
        producto=Producto(5,"Fifa 14",10,41.95)
        self.catalogo.append(producto)

    def menu(self):
        for producto in self.catalogo:
            print("{0}: {1} ${2}".format(
                producto.codigo,producto.nombre,producto.precio))

    def buscarProducto(self,numero):
        for producto in self.catalogo:
            if producto.codigo==numero:
                return producto

if __name__ == "__main__":
    tienda=Tienda()
    carro=Carro()
    while True:
        tienda.menu()
        item_ingresado=input("Ingresa un producto a comprar (numero,cantidad): ")
        if item_ingresado=="":
            break
        else:
            item_ingresado=item_ingresado.split(",")
            numero=int(item_ingresado[0])
            producto=tienda.buscarProducto(numero)
            cantidad=int(item_ingresado[1])
            carro.agregar_item(cantidad,producto)
        print(carro)

    print(carro.checkout(0,"usa"))
    print(carro.checkout(1,"usa"))
    print(carro.checkout(0,"Alameda 340 Santiago Chile"))
    print(carro.checkout(1,"Alameda 340 Santiago Chile"))
 class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class Tienda:
    def __init__(self):
        self.catalogo = [
            Producto(1, "Producto 1", 10),
            Producto(2, "Producto 2", 20),
            Producto(3, "Producto 3", 30),
            Producto(4, "Producto 4", 40),
            Producto(5, "Producto 5", 50)
        ]

    def buscarProducto(self, numero):
        for producto in self.catalogo:
            if producto.codigo == numero:
                return producto

    def menu(self):
        print("Catálogo de productos:")
        for producto in self.catalogo:
            print(f"{producto.codigo}: {producto.nombre} - ${producto.precio}")


class Carro:
    def __init__(self):
        self.items = []

    def agregar_item(self, cantidad, producto):
        self.items.append((producto, cantidad))

    def __str__(self):
        mensaje = "Carro de compras:\n"
        for item in self.items:
            producto, cantidad = item
            mensaje += f"{producto.nombre} - Cantidad: {cantidad}\n"
        return mensaje

    def calcular_descuento(self):
        descuento_total = 0
        for item in self.items:
            producto, cantidad = item
            descuento = producto.precio * cantidad * 0.1
            descuento_total += descuento
        return descuento_total

    def calcular_despacho(self, tipoDespacho):
        valor_total = self.calcular_total()
        if tipoDespacho == 0:
            return valor_total * 0.2
        elif tipoDespacho == 1:
            return valor_total * 0.3

    def calcular_total(self):
        total = 0
        for item in self.items:
            producto, cantidad = item
            total += producto.precio * cantidad
        return total

    def checkout(self, tipoDespacho, direccion):
        descuento = self.calcular_descuento()
        despacho = self.calcular_despacho(tipoDespacho)
        total = self.calcular_total() - descuento + despacho
        if "chile" in direccion.lower():
            total += total * 0.2
        return total


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
    print(carro.checkout(1, "Alameda 340 Santiago Chile"))
          