#Descomponer un número
print()
print()
Digito = int(input('Ingrese un digito de hasta 4 cifras: '))

Cifra1 = Digito%10
Cifra2 = (Digito%100)//10
Cifra3 = (Digito%1000)//100
Cifra4 = (Digito%10000)//1000

    #   UNIDAD DE MIL
if  1000 <= Digito <= 9999:
    print(str(Cifra4)+str('M')+str(' ')+str('+')+str(' ')\
      +str(Cifra3)+str('C')+str(' ')+str('+')+str(' ')\
      +str(Cifra2)+str('D')+str(' ')+str('+')+str(' ')\
      +str(Cifra1)+str('U'))
    #   CENTENAS  
if  100 <= Digito <= 999:
    print(str(Cifra3)+str('C')+str(' ')+str('+')+str(' ')\
          +str(Cifra2)+str('D')+str(' ')+str('+')+str(' ')\
          +str(Cifra1)+str('U'))
    #   DECENAS
if  10 <= Digito <= 99:
    print(str(Cifra2)+str('D')+str(' ')+str('+')+str(' ')\
          +str(Cifra1)+str('U'))
    #   UNIDADES
if  1 <= Digito <= 10:
    print(str(Cifra1)+str('U'))