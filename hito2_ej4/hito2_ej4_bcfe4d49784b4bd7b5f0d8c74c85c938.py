p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

carro = {}

def agregar_producto(producto, cantidad):
    global carro
    if producto == "1":
        if producto not in carro:
            carro[producto] = [p1[1], p1[2], cantidad]
        else:
            carro[producto][2] += cantidad
    elif producto == "2":
        if producto not in carro:
            carro[producto] = [p2[1], p2[2], cantidad]
        else:
            carro[producto][2] += cantidad
    elif producto == "3":
        if producto not in carro:
            carro[producto] = [p3[1], p3[2], cantidad]
        else:
            carro[producto][2] += cantidad
    elif producto == "4":
        if producto not in carro:
            carro[producto] = [p4[1], p4[2], cantidad]
        else:
            carro[producto][2] += cantidad
    elif producto == "5":
        if producto not in carro:
            carro[producto] = [p5[1], p5[2], cantidad]
        else:
            carro[producto][2] += cantidad
    else:
        print("Producto inválido")

def ver_carro():
    global carro
    if len(carro) == 0:
        print("Carro vacío")
    else:
        print("Productos en el carro:")
        for producto in carro:
            print("",producto,": ",carro[producto][0]," - Cantidad: ",carro[producto][2],"",sep="")

def checkout():
    global carro
    descuento1 = 0
    descuento2 = 0
    total = 0
    for producto in carro:
        if producto in ["1", "2", "3"]:
            descuento1 += carro[producto][1] * carro[producto][2]
        elif producto in ["4", "5"]:
            descuento2 += carro[producto][1] * carro[producto][2]
        total += carro[producto][1] * carro[producto][2]
    if descuento1 > 0:
        total = total - (descuento1 * 0.2)
    if descuento2 > 0:
        total = total - (descuento2 * 0.15)
    print("Total a pagar: ",round(total, 1)," USD",sep="")
    carro = {}

while True:
    orden = input("Ingrese orden (agregar, ver, checkout): ")
    if orden == "agregar":
        producto, cantidad = input("Ingrese producto y cantidad (en formato 'producto,cantidad'): ").split(",")
        agregar_producto(producto, int(cantidad))
    elif orden == "ver":
        ver_carro()
    elif orden == "checkout":
        checkout()
        break
    else:
        print("Orden inválida")
