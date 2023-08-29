print('Introduce tres números: ')
while True:
    try:
        num1 = float(input('Número 1: '))
        break
    except:
        print('El dato no es correcto. Inténtalo de nuevo.')
while True:
    try:
        num2 = float(input('Número 2: '))
        break
    except:
        print('El dato no es correcto. Inténtalo de nuevo.')
while True:
    try:
        num3 = float(input('Número 3: '))
        break
    except:
        print('El dato no es correcto. Inténtalo de nuevo.')

orden = ordenarNumeros(num1, num2, num3)

print(f'Aquí tienes los 3 números ordenados de menor a mayor: {orden[0]}, {orden[1]}, {orden[2]}')