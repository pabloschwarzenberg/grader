p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

carro = []
has_20_dcto = 0
has_15_dcto = 0
def agregar_al_carro(compra):
    global has_20_dcto
    global has_15_dcto
    prod = int(compra[0])
    cant = int(compra[2])
    
    if prod == 1:
        has_20_dcto = has_20_dcto + 1
        for x in range(cant):
            carro.append(p1)
            print(p1)
    elif prod == 2:
        has_20_dcto = has_20_dcto + 1
        for x in range(cant):
            carro.append(p2)
            print(p2)
    elif prod == 3:
        has_20_dcto = has_20_dcto + 1
        for x in range(cant):
            carro.append(p3)
            print(p3)
    elif prod == 4:
        has_15_dcto = has_15_dcto + 1
        for x in range(cant):
            carro.append(p4)
            print(p4)
    elif prod == 5:
        has_15_dcto = has_15_dcto + 1
        for x in range(cant):
            carro.append(p5)
            print(p5)

def sumar_carro():
    sum_1_2_3 = 0
    sum_4_5 = 0
    dcto_20 = 0
    dcto_15 = 0

    total = 0
    for producto in carro:
        total += producto[2]
        if producto[0] == 1:
            sum_1_2_3 += producto[2]
        if producto[0] == 2:
            sum_1_2_3 += producto[2]
        if producto[0] == 3:
            sum_1_2_3 += producto[2]
        if producto[0] == 4:
            sum_4_5 += producto[2]
        if producto[0] == 5:
            sum_4_5 += producto[2]
    print(has_20_dcto)
    if has_20_dcto == 3:
        print(total)
        dcto_20 = (total * 20)/100
    if has_15_dcto == 2:
        dcto_15 = (total * 15)/100
    print(dcto_20)
    print(round(total - dcto_15 - dcto_20, 1))


compra = input()
while compra != 'checkout':
    agregar_al_carro(compra)
    compra = input()
sumar_carro()