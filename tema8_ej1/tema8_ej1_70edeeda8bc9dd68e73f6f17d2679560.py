class CarritoDeCompras:
    def __init__(self):
        self.inventario = {
            '1': {'nombre': 'Juego Pokemon X para Nintendo 3DS', 'precio': 33.77},
            '2': {'nombre': 'Nintendo 3DS XL', 'precio': 203.0},
            '3': {'nombre': 'Juego Mario Kart 7 para Nintendo 3DS', 'precio': 27.58},
            '4': {'nombre': 'PlayStation 4', 'precio': 348.0},
            '5': {'nombre': 'FIFA 16, PlayStation 4', 'precio': 51.19},
        }
        self.carrito = {}

    def agregar_producto(self, id_producto, cantidad):
        if id_producto not in self.inventario:
            print('Producto no encontrado.')
            return
        if id_producto in self.carrito:
            self.carrito[id_producto] += cantidad
        else:
            self.carrito[id_producto] = cantidad

    def ver_carrito(self):
        for id_producto, cantidad in self.carrito.items():
            nombre = self.inventario[id_producto]['nombre']
            print('{} x{}'.format(nombre, cantidad))

    def calcular_subtotal(self, lista_productos):
        min_cantidad = min(self.carrito.get(id_producto, 0) for id_producto in lista_productos)
        descuento = sum(self.inventario[id_producto]['precio'] for id_producto in lista_productos) * min_cantidad
        no_descuento = sum(self.inventario[id_producto]['precio'] * (self.carrito.get(id_producto, 0) - min_cantidad) for id_producto in lista_productos)
        return descuento, no_descuento

    def checkout(self):
        subtotal1_descuento, subtotal1_no_descuento = self.calcular_subtotal(['1', '2', '3'])
        subtotal2_descuento, subtotal2_no_descuento = self.calcular_subtotal(['4', '5'])
        
        total = subtotal1_descuento * 0.8 + subtotal2_descuento * 0.85 + subtotal1_no_descuento + subtotal2_no_descuento
        print('Total: USD {}'.format(round(total, 1)))

# Crear el carrito de compras
carrito = CarritoDeCompras()

while True:
    comando = input('Ingrese un comando (producto,cantidad | "ver" | "checkout"): ')
    
    if ',' in comando:
        producto, cantidad = comando.split(',')
        carrito.agregar_producto(producto, int(cantidad))
    elif comando == 'ver':
        carrito.ver_carrito()
    elif comando == 'checkout':
        carrito.checkout()
        break
    else:
        print('Comando no reconocido.')