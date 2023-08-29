numero=int(input('Ingrese un número: '))
tamano = str(numero)
while len(tamano)>4:
    print('Error -> Debería ser un número de hasta 4 dígitos')
    numero=int(input('Ingrese un número: '))
c4=numero%10                                              #Unidades
c3=int((numero%100)/10)                                   #Decenas
c2=int((numero%1000)/100)                                 #Centenas
c1=int((numero%10000)/1000)                               #Millares
if c1 != 0:
    print(c1, 'M+', c2, 'C+', c3, 'D+', c4, 'U')
elif c1 == 0 and c2 != 0:
    print(c2, 'C+', c3, 'D+', c4, 'U')
elif c1 == 0 and c2 == 0 and c3 != 0:
    print(c3, 'D+', c4, 'U')
else:
    print(c4, 'U')
