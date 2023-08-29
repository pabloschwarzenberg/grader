p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]


def checkout(list):
    sum = 0
    total = 0
    for i in list:
        if i[0] == '1':
            sum += 33.77 * int(i[2])
        elif i[0] == '2':
            sum += 203 * int(i[2])
        elif i[0] == '3':
            sum += 27.58 * int(i[2])
        elif i[0] == '4':
            sum += 348.00 * int(i[2])
        elif i[0] == '5':
            sum += 51.19 * int(i[2])
    a = False
    b = False
    c = False
    d = False
    e = False
    for i in list:
        if i[0] == '1':
            a = True
        elif i[0] == '2':
            b = True
        elif i[0] == '3':
            c = True
    if a == True and b == True and c == True:
        total = round(sum * 0.8, 1)
        return total
    for i in list:
        if i[0] == '4':
            d = True
        elif i[0] == '5':
            e = True
    if d == True and e == True:
        total = round(sum * 0.85, 1)
        return total
    else:
        return round(sum, 1)


def compra(carro_de_compras):
    l = carro_de_compras
    print(l)
    l1 = l[:-1]
    print(l1)
    if l[-1] == 'agregar':
        ''
    elif l[-1] == 'ver':
        ''
    elif l[-1] == 'checkout':
        return checkout(l1)


carro_de_compras = [input(),input(),input(),input()]
print(compra(carro_de_compras))