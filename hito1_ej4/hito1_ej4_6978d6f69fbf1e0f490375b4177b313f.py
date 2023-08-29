def binarizar(d):
    Binario = ''
    while d // 2 != 0:
        Binario = str(d % 2) + Binario
        d = d // 2
    return str(d) + Binario

Número = int(input('Introduzca el número que quiera convertir a binario: '))
print(binarizar(Número))