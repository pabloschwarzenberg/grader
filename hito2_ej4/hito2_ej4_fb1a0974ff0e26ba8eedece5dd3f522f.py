class Compra:
    def __init__(self):
        self.p1=[1,"Pokemon X",33.77]
        self.p2=[2,"Nintendo XL",203]
        self.p3=[3,"Mario Kart 7",27.58]
        self.p4=[4,"PlayStation 4",348.00]
        self.p5=[5,"FIFA 16",51.19]
        self.carro = []
        self.precio_total = 0

    def agregar_producto(self,string):
        l_string = string.split(",")
        producto = int(l_string[0])
        cantidad = int(l_string[1])

        if producto == 1:
            for i in range(cantidad):
                self.carro.append(self.p1)

        elif producto == 2:
            for i in range(cantidad):
                self.carro.append(self.p2)

        elif producto == 3:
            for i in range(cantidad):
                self.carro.append(self.p3)

        elif producto == 4:
            for i in range(cantidad):
                self.carro.append(self.p4)

        elif producto == 5:
            for i in range(cantidad):
                self.carro.append(self.p5)

    def ver(self):
        return self.carro

    def checkout(self):
        for i in self.carro:
            precio = float(i[2])
            self.precio_total += precio

        if (self.p1 in self.carro) and (self.p2 in self.carro) and (self.p3 in self.carro):
            self.precio_total = self.precio_total * 0.8

        elif (self.p4 in self.carro) and (self.p5 in self.carro):
            self.precio_total = self.precio_total * 0.85


        #print("%.1f"%self.precio_total)
        return round(self.precio_total,1)

#creas la instancia de la clase
tienda = Compra()
continuar=True
while continuar:
    accion=input("Ingrese acción: ")
    accion=accion.lower()
    if "," in accion:
        tienda.agregar_producto(accion)
    elif accion=="ver":
        carro=tienda.ver()
        for producto in carro:
            print(producto)
    elif accion=="checkout":
        valor=tienda.checkout()
        print(valor)
        continuar=False