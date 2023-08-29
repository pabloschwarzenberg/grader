x = input()


def lala(x):
    l = []
    n = [1, 2, 3, 4, 5]
    for n in range(2 ** int(x)):
        l.append(n)
    return print(("hola" + "\n") * (2**int(x)))


lala(x)
           