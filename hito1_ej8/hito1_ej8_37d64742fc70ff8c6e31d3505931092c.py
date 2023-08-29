#Descomponer un número
x = str(input("Ingrese un numero de 4 digitos o menos: "))
a = [-4]
b = [-3]
c = [-2]
d = [-1]
if len(x) == 1:
    print(x+"U")
if len(x) == 2:
    print(x[-2] + "D" , "+" , x[-1] + "U")
if len(x) == 3:
    print(x[-3] + "C" , "+" , x[-2] + "D" , "+" , x[-1] + "U")
if len(x) == 4:
    print((x[-4]) + "M" , "+" , (x[-3]) + "C" , "+" , (x[-2]) + "D" , "+" , (x[-1]) + "U")