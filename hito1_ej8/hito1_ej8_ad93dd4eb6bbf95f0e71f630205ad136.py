num1 = int(input('Ingrese un numero de 4 digitos : '))
lar = len(str(num1))
if lar == 4:
    mil = num1 / 1000
    num1 = num1 % 1000
    cen = num1 / 100
    num1 = num1 % 100
    dec = num1 / 10
    uni = num1 % 10
    print('Descomposición: %dM + %dC + %dD + %dU' %(mil,cen,dec,uni))
if lar == 3:
    cen = num1 / 100
    num1 = num1 % 100
    dec = num1 / 10
    uni = num1 % 10
    print('Descomposición: %dC + %dD + %dU' %(cen,dec,uni))
if lar == 2:
    dec = num1 / 10
    uni = num1 % 10
    print('Descomposición: %dD + %dU' %(dec,uni))
if lar == 1:
    print('Descomposición: %dU' %(num1))
      