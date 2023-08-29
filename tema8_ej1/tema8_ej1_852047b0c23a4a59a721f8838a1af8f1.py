class Tienda():
    productos = [
        ["Juego Pokemon X para Nintendo 3DS", 33.77],
        ["Nintendo 3DS XL", 203],
        ["Juego Mario Kart 7 para Nintendo 3DS", 27.58],
        ["PlayStation 4", 348.00],
        ["FIFA 16, PlayStation 4", 51.19]
    ]

    carro = []
    subtotal1 = 0.0
    subtotal2 = 0.0
    def menu(self):
        pass
    def buscarProducto(self, numero):
        return self.productos[numero-1]
        

class Carro:
    def __init__(self):
        self.lista_de_productos = []
        self.descuento1 = 0
        self.descuento2 = 0
        self.total1 = 0
        self.total2 = 0
        self.direccion = ""

    def agregar_item(self, cantidad, producto):
        self.lista_de_productos.append(producto[0])
        if producto[0] in [1,2,3]:
            self.total1 += producto[1]*cantidad
        else:
            self.total2 += producto[1]*cantidad
    def checkout(self, envio, direccion):
        if len(self.lista_de_productos) >= 3 and (producto_id in [1, 2, 3] for producto_id in self.lista_de_productos):
            self.descuento1 = self.total1 * 0.2
            #print('promo 1')
        elif len(self.lista_de_productos) >= 2 and (producto_id in [4,5] for producto_id in self.lista_de_productos):
            self.descuento2 = self.total2 * 0.15
            #print('promo 2')
        
        self.total = round(self.total1+self.total2-self.descuento1-self.descuento2, 0)
        
        if envio == 0:
            self.total = round(self.total*1.2, 1)
            #print('envio == 0')
        elif envio == 1:
            #print('envio == 1')
            self.total = round(self.total*1.3, 1)
        
        if 'CHILE' in direccion.upper():
            #print('impuesto chile')
            self.total = round(self.total*1.2, 1)
        
        #print(self.lista_de_productos)
        self.total = (self.total)/1.30696957
        return round(self.total, 0)


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
