p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

productos = [p1,p2,p3,p4,p5]
carro=[0,0,0,0,0,0.0]

def agregar_carro(producto,cantidad,):
    producto = int(producto)
    cantidad = int(cantidad)
    if producto == 1:
        carro[0] += cantidad
        carro[5] += (p1[2]*cantidad)
    elif producto == 2:
        carro[1] += cantidad
        carro[5] += (p2[2]*cantidad)
    elif producto == 3:
        carro[2] += cantidad
        carro[5] += (p3[2]*cantidad)
    elif producto == 4:
        carro[3] += cantidad
        carro[5] += (p4[2]*cantidad)
    elif producto == 5:
        carro[4] += cantidad
        carro[5] += (p5[2]*cantidad)


def ver():
    for producto in productos:
        print(producto)

def checkout():
    total = 0.0
    if carro[0] > 0 and carro[1] > 0 and carro[2] > 0:
        total += ((p1[2]*carro[0])+(p2[2]*carro[1])+(p3[2]*carro[2]))*0.8
    else:
        total += (p1[2]*carro[0])+(p2[2]*carro[1])+(p3[2]*carro[2])
    if carro[3] > 0 and carro[4] > 0:
        total += ((p4[2]*carro[3])+(p5[2]*carro[4]))*0.85
    else:
        total += (p4[2]*carro[3])+(p5[2]*carro[4])
    total = round(total,1)
    print(total)

while True:
    a = input()
    if a == "ver":
        ver()
    elif a == "checkout":
        checkout()
        break
    else:
        b = a.split(",")
        agregar_carro(b[0],b[1])