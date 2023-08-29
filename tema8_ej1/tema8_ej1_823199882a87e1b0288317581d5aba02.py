class Tienda:
    def __init__(self):
        self.productos = {
            1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
            2: {"nombre": "Nintendo 3DS XL", "precio": 203.00},
            3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
            4: {"nombre": "PlayStation 4", "precio": 348.00},
            5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
        }
        self.carro = {}

    def agregar_producto(self, producto, cantidad):
        producto = int(producto)
        cantidad = int(cantidad)
        if producto in self.carro:
            self.carro[producto] += cantidad
        else:
            self.carro[producto] = cantidad
        print("Se agregaron "+str(cantidad)+" unidades del producto "+str(producto)+" al carro.")

    def ver_productos(self):
        print("Productos en el carro:")
        for producto, cantidad in self.carro.items():
            nombre = self.productos[producto]["nombre"]
            precio = self.productos[producto]["precio"]
            subtotal = precio * cantidad
            print(str(nombre)+" (x"+str(cantidad)+"): USD "+str(subtotal))

    def checkout(self, tipoDespacho, direccion):
        total_productos = 0
        impuesto = 0.2 if "chile" in direccion.lower() else 0

        for producto, cantidad in self.carro.items():
            precio = self.productos[producto]["precio"]
            subtotal = precio * cantidad
            total_productos += subtotal

        descuento = 0
        despacho = 0

        if len(self.carro) >= 3 and all(producto in self.carro for producto in [1, 2, 3]):
            descuento = total_productos * 0.2  # Descuento del 20%
        elif len(self.carro) >= 2 and all(producto in self.carro for producto in [4, 5]):
            descuento = total_productos * 0.15  # Descuento del 15%

        if tipoDespacho == 0:  # Despacho Aéreo Normal
            despacho = total_productos * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            despacho = total_productos * 0.3

        total_pagar = total_productos - descuento + despacho
        total_pagar *= (1 + impuesto)

        return total_pagar