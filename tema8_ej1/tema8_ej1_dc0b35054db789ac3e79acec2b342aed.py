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
        # Calcular el valor de los productos
        valor_productos = 0
        for item in self.lista_de_productos:
            valor_productos += item.producto.precio * item.cantidad
        
        # Calcular el valor de los descuentos
        def descuento_especial():
            # Asumir que hay un descuento del 10% si se compran los productos 2 y 3 juntos
            producto_2 = Producto(2,"Nintendo 3DS",5,190.95)
            producto_3 = Producto(3,"Juego Mario Kart",10,29.96)
            if producto_2 in [item.producto for item in self.lista_de_productos] and producto_3 in [item.producto for item in self.lista_de_productos]:
                # Calcular el precio de los productos 2 y 3
                precio_2 = producto_2.precio * [item.cantidad for item in self.lista_de_productos if item.producto == producto_2][0]
                precio_3 = producto_3.precio * [item.cantidad for item in self.lista_de_productos if item.producto == producto_3][0]
                # Aplicar el descuento del 10% al precio de los productos 2 y 3
                return (precio_2 + precio_3) * 0.1
            else:
                return 0
        
        valor_descuentos = descuento_especial()

        # Calcular el valor de los productos después de restarle el descuento
        valor_productos -= valor_descuentos

        # Calcular el valor del despacho
        if tipoDespacho == 0: # Despacho Aéreo Normal
            porcentaje_despacho = 0.2
        elif tipoDespacho == 1: # Despacho Aéreo Express
            porcentaje_despacho = 0.3
        
        valor_despacho = valor_productos * porcentaje_despacho

        # Calcular el valor total a pagar
        valor_total = valor_productos + valor_despacho

        # Agregar el impuesto del 20% si el despacho es hacia Chile
        if "chile" in direccion.lower():
            valor_total *= 1.2
        
        # Retornar el valor total redondeado a dos decimales
        return round(valor_total,2)

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

