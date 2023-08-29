p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

carro = [p1, p2, p3, p4, p5]
productos = []
descuento = 0
items = []
precios = []

print("TIENDA :")
for producto in carro:
    print(producto)

commando = input("Ingrese su commando: ")
while commando != "checkout":
    if commando == "ver":
        if not productos:
            print("Usted no tiene nada en su carro")
        else:
            print("Usted tiene en su carro: ")
            for producto in productos:
                print(producto)
    else:
        orden = [int(x) for x in commando.split(",")]
        for i in range(orden[1]):
            productos.append(carro[orden[0] - 1])
    commando = input("Ingrese su commando: ")

for producto in productos:
    items.append(producto[1])

for precio in productos:
    precios.append(precio[2])

print("Usted esta la realizando la compra de:")
for producto in productos:
    print(producto)

if 1 in items or 2 in items or 3 in items:
    descuento += 0.20
if 4 in items or 5 in items:
    descuento += 0.15

print("VALOR TOTAL = " + str(round(sum(precios) - (sum(precios) * descuento), 1)))
