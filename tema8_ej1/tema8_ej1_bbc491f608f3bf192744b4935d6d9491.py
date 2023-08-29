import modulo2 as m2

class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def mostrar(self):
        return self.nombre, " - ", self.direccion


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        return self.nombre, " - ", self.precio


class CarroDeCompras:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def eliminarProducto(self, producto):
        self.productos.remove(producto)

    def mostrar(self):
        s = ""
        for producto in self.productos:
            s += f"{producto.mostrar()[0]} - ${producto.mostrar()[2]}\n"
        return s

    def checkout(self, tipoDespacho, direccion):
        total = 0
        descuentos = 0

        # Calcular el valor de los descuentos
        for producto in self.productos:
            descuentos += producto.precio * 0.1  # Supongamos un descuento fijo del 10% para cada producto

        # Calcular el valor del despacho
        if tipoDespacho == 0:  # Despacho Aéreo Normal
            despacho = sum(producto.precio for producto in self.productos) * 0.2
        elif tipoDespacho == 1:  # Despacho Aéreo Express
            despacho = sum(producto.precio for producto in self.productos) * 0.3
        else:
            despacho = 0

        # Calcular impuesto si el despacho es hacia Chile
        if "chile" in direccion.lower():
            impuesto = (sum(producto.precio for producto in self.productos) - descuentos + despacho) * 0.2
        else:
            impuesto = 0

        total = sum(producto.precio for producto in self.productos) - descuentos + despacho + impuesto
        return total