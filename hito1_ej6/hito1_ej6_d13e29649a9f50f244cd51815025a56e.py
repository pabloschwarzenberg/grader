def ordenarNumeros(n1,n2,n3):
    lista = [n1,n2,n3]
    lista.sort()
    return lista
print('Introduce tres números: ')
while True:
    try:
        num1 = int(input('Número 1: '))
        break
    except:
        print('El dato no es correcto. Inténtalo de nuevo.')
while True:
    try:
        num2 = int(input('Número 2: '))
        break
    except:
        print('El dato no es correcto. Inténtalo de nuevo.')
while True:
    try:
        num3 = int(input('Número 3: '))
        break
    except:
        print('El dato no es correcto. Inténtalo de nuevo.')

orden = ordenarNumeros(num1, num2, num3)

print(orden[0],",",orden[1],",", orden[2])
