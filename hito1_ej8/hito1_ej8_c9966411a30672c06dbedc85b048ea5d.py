#Descomponer un número
Num = str(input("Ingrese un numero de hasta 4 digitos: "))
N1 = [-4]
N2 = [-3]
N3 = [-2]
N4 = [-1]
if len(Num) == 1:
    print(Num+"U")
if len(Num) == 2:
    print((Num[-2])+"D","+",(Num[-1])+"U")
if len(Num) == 3:
    print((Num[-3])+"C","+",(Num[-2])+"D","+",(Num[-1])+"U")
if len(Num) == 4:
    print((Num[-4])+"M","+",(Num[-3])+"C","+",(Num[-2])+"D","+",(Num[-1])+"U")
