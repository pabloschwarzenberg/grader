p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]


productos = [p1, p2, p3, p4, p5]
carrito = []

def ver():
    for elemento in productos:
        prod = ""
        for cosa in elemento:
            prod += str(cosa) + " "
        print(prod.strip())

def agregar(prod_cant):
    prod_l = prod_cant.split(",")
    prod_l[0] = int(prod_l[0])
    prod_l[1] = int(prod_l[1])
    return prod_l

def checkoutx():
    suma = 0
    cant_menor_a = 0
    cant_menor_b = 0
    objetos = []
    for ob in carrito:
        objetos.append(ob[0])

    if 1 in objetos and 2 in objetos and 3 in objetos:
        for x in range(1,4): 
            if objetos.count(x) > cant_menor_a:
                cant_menor_a = objetos.count(x)
    
    if 4 in objetos and 5 in objetos:   
        for x in range(4,6): 
            if objetos.count(x) > cant_menor_b:
                cant_menor_a = objetos.count(x)

    for elem in carrito:
        suma += productos[elem[0] - 1][2] * elem[1]

    suma -= 0.2 * (p1[2] + p2[2] + p3[2]) * cant_menor_a
    suma -= 0.15 * (p4[2] + p5[2]) * cant_menor_b

    return round(suma,1)


for x in range(4):
    entrada = str(input())
    if entrada[1] == ",":
        carrito.append(agregar(entrada))
    elif entrada == "ver":
        ver()
    elif entrada == "checkout":
        print(checkoutx())