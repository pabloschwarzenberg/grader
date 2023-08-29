#Descomponer un número
f = int(input('ingrese un numero con un maximo de 4 digitos: '))
f1 = str(f)
f2 = len(f1)
if f2 == 4:
    f3 = str(f1[0])+('M')
    f4 = str(f1[1])+('C')
    f5 = str(f1[2])+('D')
    f6 = str(f1[3])+('U')
    print(f3,'+',f4,'+',f5,'+',f6)
if f2 == 3:
    f44 = str(f1[0])+('C')
    f55 = str(f1[1])+('D')
    f66 = str(f1[2])+('U')
    print(f44,'+',f55,'+',f66)
if f2 == 2:
    f77 = str(f1[0])+('D')
    f88 = str(f1[1])+('U')
    print(f77,'+',f88)
if f2 == 1:
    f99 = str(f1[0])+('U')
    print(f99)
     