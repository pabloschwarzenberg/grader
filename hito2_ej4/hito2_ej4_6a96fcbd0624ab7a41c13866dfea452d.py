productos = {
    "1": ("Pokemon X", 33.77),
    "2": ("Nintendo XL", 203),
    "3": ("Mario Kart 7", 27.58),
    "4": ("PlayStation 4", 348.00),
    "5": ("FIFA 16", 51.19),
}


class Carro:
    def __init__(self):
        self.lista_compra = []
        self.valor_carro = 0

    def agregar_productos(self):
        producto, cantidad = input().replace(" ", "").split(",")
        for _ in range(int(cantidad)):
            nombre, precio = productos[producto]
            self.lista_compra.append(nombre)
            self.valor_carro = self.valor_carro + precio

    def ver(self):
        print("Productos")
        for k, v in productos.items():
            print(str(k) + ": " + str(v[0]))

    def checkout(self):
        subtotal = self.valor_carro
        descuento_a = 0
        descuento_b = 0

        if (
            productos["1"] in self.lista_compra
            and productos["2"] in self.lista_compra
            and productos["3"] in self.lista_compra
        ):
            descuento_a = (
                productos["1"][1] + productos["2"][1] + productos["3"][1]
            ) * 0.2
        if productos["4"] in self.lista_compra and productos["5"] in self.lista_compra:
            descuento_a = (productos["4"][1] + productos["5"][1]) * 0.15

        print(round(subtotal - descuento_a - descuento_b, 1))
        return round(subtotal - descuento_a - descuento_b, 1)

if __name__ == "__main__":
  pass