#Descomponer un número
numero = str(input('Ingrese numero a descomponer :'))
if len(numero) == 1:
    print(numero , 'U')
elif len(numero) == 2:
    print(numero[0] , 'D + ', numero[1], 'U')
elif len(numero) == 3:
    print(numero[0], 'C +', numero[1] , 'D + ', numero[2], 'U')
elif len(numero) == 4:
    print(numero[0], 'M +', numero[1], 'C +', numero[2] , 'D + ', numero[2], 'U')