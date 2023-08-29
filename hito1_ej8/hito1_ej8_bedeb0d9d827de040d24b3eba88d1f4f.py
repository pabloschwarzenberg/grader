#Descomponer un número
num = int(input("Introduce el número: "))
numStr = str(num)

num1 = numStr[0]
num2 = numStr[1]
num3 = numStr[2]

if num > 999:
    num4 = numStr[3]
    unidad = num4 + 'U'

mil = num1 +'M'
centena = num2 +'C'
decena = num3 +'D'

if num > 999:
    print(mil,'+', centena,'+', decena,'+', unidad)
else:
    cent = num1 + 'C'
    dec = num2 + 'D'
    uni = num3 + 'U'

    print(cent,'+', dec,'+', uni)     