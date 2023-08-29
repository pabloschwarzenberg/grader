# completa el código de la función
def suma_divisores(a):
    lista = []
    if a > 1:
        for n in range(1, a):
            if a % n == 0:
                lista.append(n)
    suma = sum(lista)
    print(suma)
    if suma == 1:
        flag = True
    else:
        flag = False
    if flag:
        return suma, True
    elif not flag:
        return suma, False

