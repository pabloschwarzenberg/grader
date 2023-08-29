p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

list1 = [p1, p2, p3, p4, p5]
items = []

def agregar(producto, cantidad):
    for num in range(cantidad):
        items.append(producto)

def ver():
    print(items)

def checkout():
    price = 0
    for item in items:
        price += list1[item-1][2]

    if 1 in items and 2 in items and 3 in items:
        price = price*0.8
    elif 4 in items and 5 in items:
        price = price*0.85
    print(round(price, 1))


if __name__ == "__main__":
    input1 = input('Ingrese algo: ')

    input1 = input1[1: len(input1) - 1]

    index = 0

    while index < len(input1):
        if input1[index] == "," and input1[index - 1] == "'":
            input1 = input1.replace(input1[index:index + 2], '*')
        index += 1

    input1 = input1.split('*')

    index = 0
    while index < len(input1):
        input1[index] = input1[index][1: len(input1[index]) - 1]
        index += 1

    for orden in input1:

        if orden == 'ver':
            ver()

        elif orden == 'checkout':
            checkout()

        else:
            orden_splitted = orden.split(',')
            if len(orden_splitted) == 2:
                agregar(int(orden_splitted[0]), int(orden_splitted[1]))