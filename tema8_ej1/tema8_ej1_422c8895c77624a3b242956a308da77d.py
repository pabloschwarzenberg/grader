class CarroDeCompras:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))
    def ver_carro(self):
        if len(self.productos) == 0:
            print("Carro vacío")
        else:
            for producto, cantidad in self.productos:
                print("Producto {}: {} - {} unidades".format(producto[0], producto[1], cantidad))
    def calcular_total(self):
        total = 0.0
        for producto, cantidad in self.productos:
            total += producto[2] * cantidad
        return total
    def aplicar_descuento(self, total):
        descuento = 0.0
        if (1 in [producto[0] for producto, _ in self.productos]) and \
           (2 in [producto[0] for producto, _ in self.productos]) and \
           (3 in [producto[0] for producto, _ in self.productos]):
            descuento = total * 0.2
        elif (4 in [producto[0] for producto, _ in self.productos]) and \
             (5 in [producto[0] for producto, _ in self.productos]):
            descuento = total * 0.15
        return descuento
    def calcular_despacho(self, total, tipoDespacho, direccion):
        despacho = 0.0
        if tipoDespacho == 0:
            despacho = total * 0.2
        elif tipoDespacho == 1:
            despacho = total * 0.3
        if "chile" in direccion.lower():
            despacho += despacho * 0.2
        return despacho
    def checkout(self, tipoDespacho, direccion):
        total = self.calcular_total()
        if total > 0:
            descuento = self.aplicar_descuento(total)
            despacho = self.calcular_despacho(total, tipoDespacho, direccion)
            total_pagar = total - descuento + despacho
            total_pagar += total_pagar * 0.2  # Agregar impuesto del 20%
            return total_pagar
        else:
            return 0.0

# Ejemplo de uso
p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

carro = CarroDeCompras()
carro.agregar_producto(p1, 2)
carro.agregar_producto(p2, 1)
carro.agregar_producto(p3, 3)

tipo_despacho = 0
direccion = "Alameda 340 Santiago Chile"
total_pagar = carro.checkout(tipo_despacho, direccion)
print("Total a pagar: {:.2f}".format(total_pagar))






    

           