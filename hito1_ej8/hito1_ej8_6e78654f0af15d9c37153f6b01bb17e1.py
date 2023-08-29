#Descomponer un número
Numero= (input('Ingrese un numero de hasta 4 digitos: '))
if len(Numero)== 4:
    print ((((Numero[0]+'M+')+ Numero[1]+'C+')+ Numero[2]+'D+')+ Numero[3]+'U')
if len(Numero)== 3:
    print (((Numero[0]+'C+')+ Numero[1]+'D+')+ Numero[2]+'U')
if len(Numero)== 2:
    print ((Numero[0]+'D+')+ Numero[1]+'U')
if len(Numero)== 1:
    print (Numero[0]+'U')
