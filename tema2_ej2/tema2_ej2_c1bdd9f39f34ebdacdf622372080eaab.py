# completa el código de la función
def amigos(x,y):
    divi = [1]
    divi_y = [1]

    for i in range(2, x + 1):
        if x % i == 0:
            divi.append(i)

    for i in range(2, y + 1):
        if y % i == 0:
            divi_y.append(i)

    if x != y:
        if sum(divi) == sum(divi_y):
            return True

        else:
            return False

    elif x == y:
        if sum(divi) == sum(divi_y):
            return False
    else:
        return False

x = int()
y = int()
resultado =(amigos(x,y))
print(resultado)          