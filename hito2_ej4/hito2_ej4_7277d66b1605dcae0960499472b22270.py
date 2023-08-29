class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto_cantidad):
        producto_id, cantidad = map(int, producto_cantidad.split(","))
        producto = next((p for p in self.productos if p["id"] == producto_id), None)
        if producto:
            producto_actualizado = {
                "id": producto["id"],
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": cantidad
            }
            self.productos.append(producto_actualizado)
        else:
            print("El producto no existe en la lista de productos.")

    def ver_productos(self):
        for producto in self.productos:
            {"id": 3, "nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 29.99},

    def obtener_total(self):
        total = 0.0
        for producto in self.productos:
            total += producto["precio"] * producto["cantidad"]

        # Aplicar descuentos
        if self.tiene_descuento_conjunto():
            total -= self.calcular_descuento_conjunto()
        elif self.tiene_descuento_individual():
            total -= self.calcular_descuento_individual()
        return round(total, 1)

    def tiene_descuento_conjunto(self):
        ids = [producto["id"] for producto in self.productos]
        return set(ids) == {1, 2, 3} or set(ids) == {4, 5}

    def calcular_descuento_conjunto(self):
        total = self.obtener_total()
        if set([1, 2, 3]).issubset([producto["id"] for producto in self.productos]):
            descuento = total * 0.20  # Descuento del 20% para productos 1, 2 y 3 juntos
        else:
            descuento = total * 0.15  # Descuento del 15% para productos 4 y 5 juntos
        return descuento

    def tiene_descuento_individual(self):
        ids = [producto["id"] for producto in self.productos]
        return set(ids) <= {1, 2, 3, 4, 5}

    def calcular_descuento_individual(self):
        descuento = 0.0
        for producto in self.productos:
            if producto["id"] in [1, 2, 3]:
                descuento += producto["precio"] * producto["cantidad"] * 0.20  # Descuento del 20% para productos 1, 2 y 3 individualmente
            elif producto["id"] in [4, 5]:
                descuento += producto["precio"] * producto["cantidad"] * 0.15  # Descuento del 15% para productos 4 y 5 individualmente
        return descuento

   def ver_productos(self):
    for producto in self.productos:
        print(f"Producto: {producto['nombre']} - Cantidad: {producto['cantidad']}")



# Crear productos
productos = [
    {"id": 1, "nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    {"id": 2, "nombre": "Nintendo 3DS XL", "precio": 203},
    {"id": 3, "nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 29.99},
    {"id": 4, "nombre": "PlayStation 5", "precio": 499.99},
    {"id": 5, "nombre": "Juego The Last of Us Part II para PlayStation 4", "precio": 39.99}
]

# Crear carrito de compras
carrito = CarritoDeCompras()

# Agregar productos al carrito
carrito.agregar_producto("1, 2")
carrito.agregar_producto("3, 1")
carrito.agregar_producto("4, 1")
carrito.agregar_producto("5, 2")

# Ver productos en el carrito
carrito.ver_productos()

# Realizar checkout
carrito.checkout()
