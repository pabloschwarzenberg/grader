numero = int(input("Introduce el número: "))
numeroStr = str(numero)

num1 = numeroStr[0]
num2 = numeroStr[1]
num3 = numeroStr[2]
if numero>999:
    num4 = numeroStr[3]
    uniStr = num4 + 'U'

milStr = num1 +'M'
cenStr = num2 +'C'
decStr = num3 +'D'

if numero > 999:
    print(milStr,'+', cenStr,'+', decStr,'+', uniStr)
else:
    cent = num1 + 'C'
    dec = num2 + 'D'
    uni = num3 + 'U'

    print(cent,'+', dec,'+', uni)